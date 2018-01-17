from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import createticket
def index(request):
    # return HttpResponse("Go Ahead create a ticket");
    tickets = createticket.objects.all()[:10]

    context = {
        'Subject': 'Tickets',
        'tickets': tickets
    }

    return render(request, 'createticket/cticket.html',context)
def details(request,id):
    ticket = createticket.objects.get(ticketId = id)
    context = {
        'ticket': ticket
    }
    return render(request, 'createticket/cdetails.html', context)