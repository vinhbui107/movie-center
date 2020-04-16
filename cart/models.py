from django.db import models
from movie.models import Movie
from account.models import CustomerUser


class Cart(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    items = models.ManyToManyField(Movie)