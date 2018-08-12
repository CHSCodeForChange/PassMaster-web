from django.db import models
from django.contrib.auth.models import User

class Conversation(models.Model):
    userOne = models.ForeignKey( # the first membber of the chat
        User,
        on_delete=models.CASCADE,
        related_name='userOne'
    )

    userTwo = models.ForeignKey( # the second member of the chat
        User,
        on_delete=models.CASCADE,
        related_name='userTwo'
    )

    # returns whether of not a specified user is part of a chat
    def is_member(self, user):
        return self.userOne == user or self.userTwo == user

    def get_messages(self, user):
        if self.is_member(user):
            return self.messages

    # returns the messages a user sent
    def sent_messages(self, user):
        if self.is_user(user): 
           return self.messages.filter(sender=user)

    # returns the messages a user recieved
    def recieved_messages(self, user):
        if self.is_user(user):
            return self.messages.exclude(sender=user)

    def get_user_conversations(user):
        return Conversation.objects.filter(userOne=user) | Conversation.objects.filter(userTwo=user)



class Message(models.Model):
    conversation = models.ForeignKey( # the conversation objejct that the message is connected to
        Conversation,
        related_name='messages',
        on_delete=models.CASCADE,
    )

    sender = models.ForeignKey( # the user that sent the message
        User, 
        on_delete=models.CASCADE,
    )

    datetime = models.DateTimeField() # datetime the message was sent

    message = models.TextField(max_length=240) # message text