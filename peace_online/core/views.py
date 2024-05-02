from django.shortcuts import render
from item.models import Category, Item

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