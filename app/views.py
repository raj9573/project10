from django.shortcuts import render

# Create your views here.
from app.forms import *

from django.http import HttpResponse
def home(request):

    uf = UserForm()

    if request.method == 'POST':
        ufd = UserForm(request.POST)

        if ufd.is_valid():
            
            return HttpResponse("Data is validated")

        else:

            return HttpResponse("Data is not validated")




    return render(request,'home.html',{'uf':uf})