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

def room(request):
    #return HttpResponse('ROOM')
    return render(request, 'base/room.html')


