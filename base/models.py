from django.db import models

class Room(models.Model):
    #host
    #topic
    name = models.CharField( max_length=50)
    description = models.TextField(null = True, blank = True)
    #participants
    updated = models.DateTimeField(auto_now = True) 
    created = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.name
    

class Message(models.Model):
    #user
    room = models.ForeignKey(Room, on_delete = models.CASCADE)#on_delete = models.NULL keeps the messages.
    body = models.TextField()
    updated = models.DateTimeField(auto_now = True) 
    created = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.body[0:50]