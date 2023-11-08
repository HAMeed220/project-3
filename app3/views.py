from django.shortcuts import render


from django.http import HttpResponse


# Create your views here.

def mahesh(request):
    return HttpResponse("<h1><marquee>'how is work in job'<h1><marquee>" )

