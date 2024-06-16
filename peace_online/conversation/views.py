from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404

from item.models import Item
from .forms import ConversationMessageForm
from .models import Conversation

@login_required
def new_conversation(request, item_pk): # primary key here is for the Item
    item = get_object_or_404(Item, pk=item_pk)
    
    if item.created_by == request.user:
        return redirect('dashboard:index', pk=conversation.first().id)
    
    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id]) # get all the conversation where you are memmber, so the request.user.id checks if the id is one of the members in members_in
    
    if conversations.exists():
        return redirect('conversation:detail')
        # return redirect('conversation:detail', pk=conversations.first().pk)  # Assuming there's a conversation detail view
    
    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        
        if form.is_valid(): # if contact field is filled out correctly
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user) # adding the current user to the members list
            conversation.members.add(item.created_by) # adding the owner to the members list
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

@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id]) # get all the conversation where you are memmber, so the request.user.id checks if the id is one of the members in members_in
    
    context = {'conversations': conversations}
    return render(request, 'conversation/inbox.html')

@login_required
def detail(request, pk): # conversation primary key not item
    conversations = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk) # get all the conversation you have first 
    
    if request.method == 'POST':
        form = ConversationMessageForm(requset.POST)
        
        if form.is_valid:
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
            
            conversation.save()
            
            return redirect('conversation:detail', pk=pk)
        
    else:
        form = ConversationMessageForm()

    
    context = {'conversation': conversation, 'form': form}
    return render(request,'conversation/detail.html', context)