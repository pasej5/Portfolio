from django.shortcuts import render, redirect
from item.models import Category, Item 

from .forms import SignupForm

# Create your views here.
def index(request):
    """information about the browser"""
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    
    context = {'categories': categories, 'items': items}
    return render(request, 'core/index.html', context)


def contact(request):
    """contacts"""
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == "POST": # if method is post we know the form has been submited then we need creat a new instance of the form
        form = SignupForm(request.POST)
        # then we take all the information from the form
        if form.is_valid():
            # check if the form has correct values and no errors
            form.save() # then the user will be created in the database
            return redirect('/login')
    else:
            form = SignupForm()
    
    
    context = {'form': form}
    return render(request, 'core/signup.html', context)