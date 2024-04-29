from django.shortcuts import render

# Create your views here.
def index(request):
    """information about the browser"""
    return render(request, 'core/index.html')


def contact(request):
    """contacts"""
    return render(request, 'core/contact.html')
