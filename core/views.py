from django.shortcuts import render, redirect
# importing the database models here so that we can use them
from item.models import Category, Item
from .forms import SignupForm
from django.contrib.auth import logout
from django.contrib import messages


# Create your views here.
def index(request):
    # tbh i really don't know why this error is occuring it is absolutely correct
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request, "core/index.html", {
                  "categories": categories,
                  "items": items,
    })


def contact(request):
    return render(request, 'core/contact.html')


def signup(request):
    if request.method == "POST":
        # when post SignupForm will take post as a parameter
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login/")
    else:
        # rendering the form with SignupForm when the method is get
        form = SignupForm()

    # when if is not true automatically the method is get and signup is created
    return render(request, 'core/signup.html' ,{
        "form": form
    })


def logout_user(request):
    logout(request)
    messages.success(request, ('You were logged out'))
    return redirect('core:index')

