from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url="/accounts/login/")
def dashboard(request):

    

    context = {
        'page_title' : 'Dashboard'
    }

    
    return render(request,'pages/index.html', context)