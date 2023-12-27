from django.shortcuts import render

from .models import Room
from .form import RoomForm

def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context)  

def room(request):
    room = Room.objects.get(id)
    context = {'rooms':room}
    return render(request,'base/room.html', context)

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()        
    context = {'form':form}
    return render(request,'base/room_form.html', context)