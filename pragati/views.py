from django.shortcuts import render
from .models import feedback
from datetime import date
# Create your views here.


def index(request):
    return render(request,'webpages/index.html')

def about(request):
    return render(request, 'webpages/about.html')

def landing(request):
    return render(request, 'webpages/landing.html')

def feedback(request):
    try:
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            subject = request.POST['subject']
            message = request.POST['message']

            msg_data = feedback(email = email,
                                name = name,
                                subject = subject,
                                message = message,
                                msg_id = 0,
                                date = date.today(),
                                )

            msg_data.save()
            return render(request, 'webpages/landing.html', {'data': "Successfuly Sent !"})

    except:
        return render(request, 'webpages/landing.html', {'data': "Internal error occured !"})
