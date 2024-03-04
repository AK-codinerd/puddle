from django.db import models
# i actually want a reference to item so I imported it
from item.models import Item
from django.contrib.auth.models import User


class Conversation(models.Model):
    # so making the item reference
    item = models.ForeignKey(Item, related_name="conversations", on_delete=models.CASCADE)
    # as there are many members who are going to talk about the item so many to many tbh i believe this should be one
    # to many but either way lets just go with this for now
    members = models.ManyToManyField(User, related_name='conversations')
    # this will add the date and time when it is created
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-modified_at',)


# this is the message thing that we are going to do
class ConversationMessage(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)



