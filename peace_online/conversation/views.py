from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404

from item.models import Item
from .forms import ConversationMessageForm
from .models import Conversation

def new_conversation(request, item_pk): # primary key here is for the Item
    item = get_object_or_404(Item, pk=item_pk)
    
    if item.created_by == request.user:
        return redirect('dashboard:index')
    
    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id]) # get all the conversation where you are memmber, so the request.user.id checks if the id is one of the members in members_in
    
    if conversations.exists():
        return redirect('conversation:detail', pk=conversations.first().pk)  # Assuming there's a conversation detail view
    
    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        
        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()
            
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
            
            return redirect('item:detail', pk=item_pk)
    else:
        form = ConversationMessageForm()
        
    context = {'form': form}
    return render(request, 'conversation/new.html', context)
