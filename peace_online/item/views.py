from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import NewItemForm, EditItemForm
from .models import Item

# Create your views here.
def detail(request, pk):
    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        raise Http404("Item does not exist")
    
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    
    context = {'item': item, 'related_items': related_items}
    return render(request, 'item/detail.html', context)


@login_required
def new(request):
    if request.method =="POST":
        
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)# this will create a database but not save it
            item.created_by = request.user # this time the user is alwaya authenticated because we have the @login required
            item.save()
            
            return redirect('item:detail', pk=item.id) #redirect the user back to the page just created
    else:
        form = NewItemForm()
        
    context = {'form': form, 'title': 'New item'}
    return render(request, 'item/form.html', context)


@login_required
def edit(request, pk):
    try:
        item = Item.objects.get(pk=pk, created_by=request.user) #get the item from the database, pk=pk from the url, created_by=request.user= this is for you to get only the items you created
    except Item.DoesNotExixt:
        raise Http404("Item does not exist or you do not have permission to delete it.")
    if request.method =="POST":
        
        form = EditItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            return redirect('item:detail', pk=item.id) #redirect the user back to the page just created
    else:
        form = EditItemForm(instance=item)
        
    context = {'form': form, 'title': 'Edit item'}
    return render(request, 'item/form.html', context)


@login_required
def delete(request, pk): #pk will be the id of the item we want to delete
    try:
        item = Item.objects.get(pk=pk, created_by=request.user) #get the item from the database, pk=pk from the url, created_by=request.user= this is for you to get only the items you created
    except Item.DoesNotExixt:
        raise Http404("Item does not exist or you do not have permission to delete it.")
    item.delete() # to delete
    
    return redirect('dashboard:index')