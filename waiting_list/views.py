from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.models import User
from userprofile.models import UserProfile
from books.models import Book
from .models import WaitingList
from django.contrib import messages
from django.utils import timezone
from django.http import HttpResponseRedirect


# Create your views here.
def join_waiting_list(request, pk):
    add_wl_book = get_object_or_404(Book,pk=pk)

    if request.method == 'POST':
        user = request.user
        waiting_list = WaitingList.objects.create(
            wl_book = add_wl_book,
            date_joined = timezone.now(),
        )      
        waiting_list.wl_user.add(user)
        waiting_list.save() 
    

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
