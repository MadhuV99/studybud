from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

rooms = [
    {'id': 1, 'name': 'Lets cook chinese!'},
    {'id': 2, 'name': 'Pad Thai, Anybody '},
    {'id': 3, 'name': 'Lets try Meditteranean!'},
]


def home(request):
    #return HttpResponse('Home page')
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    #return HttpResponse('ROOM')
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    return render(request, 'base/room.html', context)


