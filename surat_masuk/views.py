from django.shortcuts import render


# Create your views here.
def surat_masuk(request):

    if request.user.is_authenticated:

        if request.user.groups.filter(name="ADMIN_TU").exists():

            context = {"page_title": "Admin - xx"}

            return render(request, "pages/surat_masuk/admin/admin.html", context)

        elif request.user.groups.filter(name="KASUBBAG_TU").exists():

            return render(request, "pages/dashboard/kasubbag.html")

        elif request.user.groups.filter(name="USER").exists():
            
            return render(request, "pages/dashboard/user.html")

        else:

            context = {"page_title": "SUPER ADMIN"}

            return render(request, "pages/dashboard/super_admin.html", context)

    else:
        pass
