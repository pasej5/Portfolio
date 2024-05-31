from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .form import NewItemForm
from .models import Item

# Create your views here.
def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
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
    