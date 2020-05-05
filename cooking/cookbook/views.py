from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return HttpResponse("Hello world")


def hello_template(request):
    context = {'name': 'Iris'}
    return render(request, 'hello.html', context)
