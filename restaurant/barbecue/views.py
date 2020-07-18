from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, "barbecue/index.html")

def about(request):

    return render(request, "barbecue/about.html")

def menu(request):

    return render(request, "barbecue/menu.html")

def reservation(request):

    #open a default page
    if(request.method == 'GET'):
        return render(request, "barbecue/reservation.html")
    else:
        time_reserve = request.POST['time_reserve']
        date_reserve = request.POST['date_reserve']    

        return render(request, "barbecue/confirm.html", {

            'time_reserve':time_reserve,
            'date_reserve':date_reserve

        })
    

