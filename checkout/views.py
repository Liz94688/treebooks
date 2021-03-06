from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from books.models import Book
from waiting_list.models import WaitingList
from userprofile.models import UserProfile
from django.contrib.auth.models import User
from home.models import TotalRaised
import stripe

# Create your views here.

stripe.api_key = settings.STRIPE_SECRET

'''
The user will need to be logged in
in order to make a payment
'''
@login_required
def checkout(request):
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
        
            cart = request.session.get('cart',{})
            total = 0
            deposit = 5
            for id, days in cart.items():
                book = get_object_or_404(Book, pk=id)
                total += (days * book.price_day) + deposit
                order_line_item = OrderLineItem(
                    order = order,
                    book = book,
                    days = days
                )
                order_line_item.save()
            
            try:
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = 'GBP',
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
            
            # timedelta - https://stackoverflow.com/questions/27491248/django-default-timezone-now-delta
            if customer.paid:
                messages.error(request, "You have succesfully paid")
               
                cart = request.session.get('cart',{})
                total_raised = 0
                books_count = 0

                for id, days in cart.items():
                    book = get_object_or_404(Book, pk=id)
                    total_raised += days * book.price_day
                    books_count += 1

                '''add payment to total money raised
                and increment number of books rented'''
                raised = get_object_or_404(TotalRaised, id=1)
                raised.money_raised += total_raised
                raised.number_books += books_count
                raised.save()

                profile = UserProfile.objects.get(user = request.user)
                              
                for id, days in cart.items():
                    book = get_object_or_404(Book, pk=id)
                    '''save book in list of read books'''
                    profile.read_books.add(book)
                    '''save book in list of current_books'''
                    profile.current_books.add(book)
                    '''update return date based on the number of days rented'''
                    book.return_date = order.date + timezone.timedelta(days=days)
                    '''set status of book as not available'''
                    book.available = False
                    book.save()

                    ''' If before renting the book the current user was in the 
                    waiting list for the book once the payment is done remove 
                    user from the waiting list'''
                    waiting_list_exist =  WaitingList.objects.filter(wl_book__id=book.id, wl_user__email=request.user.email).exists()
                    if waiting_list_exist:
                        waiting_list =  WaitingList.objects.get(wl_book__id=book.id, wl_user__email=request.user.email)
                        waiting_list.wl_user.remove(request.user)

                # clear cart
                request.session['cart'] = {}
                return redirect(reverse('view_all_books'))
            
            else:
                messages.error(request, "Unable to make payment")
    
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    
    # if method is not POST
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()

    return render(request, 'checkout.html', {'payment_form':payment_form, 'order_form':order_form, 'publishable':settings.STRIPE_PUBLISHABLE})
