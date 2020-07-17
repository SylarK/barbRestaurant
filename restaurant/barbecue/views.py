from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, "barbecue/index.html")

def about(request):

    return render(request, "barbecue/about.html")

def menu(request):

    return render(request, "barbecue/menu.html")

def reservation(request):
    
    return render(request, "barbecue/reservation.html")

