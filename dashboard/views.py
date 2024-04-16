from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect, get_object_or_404


@login_required(login_url="/accounts/login/")
def dashboard(request):

    if request.user.is_authenticated:

        if request.user.groups.filter(name="ADMIN_TU").exists():

            context = {"page_title": "Admin - Dashboard"}

            return render(request, "pages/dashboard/admin.html", context)

        elif request.user.groups.filter(name="KASUBBAG_TU").exists():

            return render(request, "pages/dashboard/kasubbag.html")

        elif request.user.groups.filter(name="USER").exists():

            return render(request, "pages/dashboard/user.html")

        else:

            context = {"page_title": "SUPER ADMIN"}

            return render(request, "pages/dashboard/super_admin.html", context)

    else:
        pass



