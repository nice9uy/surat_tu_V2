from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

@login_required(login_url="/accounts/login/")
def dashboard(request):

    if request.user.is_authenticated:

        list_group = list(request.user.groups.all())
        grup_name = [group.name for group in list_group]

        try:
            
            group1  = grup_name[0]
            group2  = grup_name[1]

        except:
            pass

        # print(grup_name)

        if request.user.groups.filter(name = "SET_TU").exists():

            context = {"page_title": "Admin - Dashboard"}

            return render(request, "pages/dashboard/admin.html", context)

        elif request.user.groups.filter(name = "TU_SET_KASUBBAG").exists():

            return render(request, "pages/dashboard/kasubbag.html")
        

        # elif request.user.groups.filter(Q(name = group1 ) & Q(name = group2 )).exists():

        #     print("xxxxxx")

        #     return render(request, "pages/dashboard/user.html")

        else:

            context = {"page_title": "SUPER ADMIN"}

            return render(request, "pages/dashboard/super_admin.html", context)

    else:
        pass



