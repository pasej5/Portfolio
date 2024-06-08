from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from item.models import Item

@login_required
def index(request):# request stands for HTTP request what the user is requesting or sending to the backend
    items = Item.objects.filter(created_by=request.user)  # get all the items you have created
    
    #then render the template
    context = {'items': items}
    return render(request, 'dashboard/index.html')


    
    
    