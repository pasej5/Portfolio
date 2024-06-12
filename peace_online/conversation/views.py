from django.shortcuts import render, redirect

from item.models import Item

from .forms import ConvesationMessageForm
from .models import Conversation

def new_conversation(request, item_pk): # primary key here is for the Item
    try:
        item = Item.objects.get(item_pk=item_pk)
    except Item.DoesNotExist:
        raise Http404('Item does not exist')
    
    if item.created_by == request.user:
        return redirect('dashboard:index')
    
    conversations = Conversation.objects.filter(item=item).filter(members__in=request.user.id)