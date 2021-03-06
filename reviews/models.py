from django.db import models
from django.contrib.auth.models import User
from books.models import Book
from django.utils import timezone

'''
The ReviewBook model will have OnetoMany relationship with the 
models User and Book
'''
# Create your models here.

class ReviewBook(models.Model):

    CHOICES = [(i,i) for i in range(0,6)]

    review_title = models.CharField(max_length=35, null=False, blank=False, default="")
    comment = models.TextField(blank=False,default="")
    score = models.IntegerField(blank=False, choices=CHOICES)
    review_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    review_author = models.ForeignKey(User, null=True, related_name="review_author", on_delete=models.SET_NULL)
    reviewed_book = models.ForeignKey(Book, default='', on_delete=models.CASCADE)
    # this field is needed for the start rating
    percentage_score =models.IntegerField(default=0)
    
    def __str__(self):
        return "{0} - {1}, {2}".format(self.score, self.reviewed_book.title, self.review_author)  
    
    class Meta:
       ordering = ('reviewed_book','-score',)