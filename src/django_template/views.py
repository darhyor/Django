from django.shortcuts import render
from .models import BookStore


def home_view(request):
    food = "Bread"
    return render(
        request,
        "home.html",
        {"food": food}
    )
