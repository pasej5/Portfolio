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
    
    if conversations:
        pass # redirect to conversation
    
    if request.method == 'POST':
        form = ConvesationMessageForm(request.POST)
        
        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()
            
            conversation_message = form.save(commit=False)
            conversation_message.conversation =conversation
            
            conversation_message.created_by = request.user