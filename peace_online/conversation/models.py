from django.contrib.auth.models import User
from django.db import models
from item.models import Item # this will reeference to the Item

class Conversation(models.Model):
    item = models.ForeignKey(Item, related_name='conversations', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='conversation') # this is because the conversation needs a lot of users the owner and the one contacting you, we pass in the user object..
    created_at = models.DateTimeField(auto_now_add=True) # this shows us when this was created
    modified_at = models.DateTimeField(auto_now=True) #when it was modified
    
    class Meta:
        ordering = ('-modified_at',)
        
class ConversationMessage(models.Model): # we cant use message because it will crash with the in built django function
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE) 
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # this shows us when this was created
    created_by = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)
    
    # always update the data base if you make changes in this file 

    
    
    