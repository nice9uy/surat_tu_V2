from django.shortcuts import render
from setting.models import DbJenisSurat


# Create your views here.
def surat_masuk(request):

    if request.user.is_authenticated:

        if request.user.groups.filter(name="ADMIN_TU").exists():

            jenis_surat_data = list(DbJenisSurat.objects.all().values_list('jenis_surat' , flat=True))


            context = {
                "page_title"  : "Admin - xx",
                'jenis_surat' : jenis_surat_data 
            }



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


def tambah_surat_masuk(request):
    return render(request, "pages/surat_masuk/admin/tambah_surat_masuk.html")
    