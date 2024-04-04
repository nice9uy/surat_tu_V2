from django.shortcuts import render

# Create your views here.
def surat_masuk_admin(request):

    context = {
                'page_title' : 'Admin - Surat Masuk'
            }

    return render(request,'pages/dashboard/admin.html', context)