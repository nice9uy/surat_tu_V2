from django.shortcuts import redirect, render,get_object_or_404
from .models import DbKlasifikasi,DbJenisSurat,DbDerajatSurat
from django.contrib.auth.decorators import login_required


@login_required(login_url="/accounts/login/")
def klasifkasi(request):
    klasifikasi_data = DbKlasifikasi.objects.all().values()

    context = {
        "page_title" : "KLASIFIKASI", 
        "klasifikasi": klasifikasi_data
        }

    return render(request, "pages/setting/klasifikasi/index.html", context)

@login_required(login_url="/accounts/login/")
def tambah_klasifikasi(request):

    if request.method == "POST":
        get_klasifikasi     = request.POST.get("tambah_klasifikasi")
        
        tambah_klasifikasi_surat = DbKlasifikasi(
            klasifikasi = get_klasifikasi,
        )

        tambah_klasifikasi_surat.save()
        return redirect("klasifkasi")

@login_required(login_url="/accounts/login/")
def edit_klasifikasi(request , id_klasifikasi ):
    edit_klasifikasi = get_object_or_404(DbKlasifikasi, pk = id_klasifikasi)
    
    if request.method == 'POST':
        get_klasifikasi        = request.POST.get('edit_klasifikasi')
            
        edit_klasifikasi = DbKlasifikasi(
                id             = id_klasifikasi,
                klasifikasi    = get_klasifikasi,        
        )
            
        edit_klasifikasi.save()
        return redirect('klasifkasi')
        
    return render(request, "pages/setting/klasifikasi/index.html")
 
@login_required(login_url="/accounts/login/")
def delete_klasifikasi(request , id_klasifikasi):
    delete_klasifikasi = get_object_or_404(DbKlasifikasi, pk = id_klasifikasi)

    if request.method == 'POST':
        delete_klasifikasi.delete()

        return redirect('klasifkasi')
#############################################################################################  
  
@login_required(login_url="/accounts/login/")
def jenis_surat(request):
    jenis_surat_data = DbJenisSurat.objects.all().values()

    # print(jenis_surat_data)

    context = {
        "page_title"   : "JENIS SURAT", 
        "jenis_surat"  : jenis_surat_data
        }
    return render(request, "pages/setting/jenis_surat/index.html", context)

    
@login_required(login_url="/accounts/login/")
def tambah_jenis_surat(request):

    if request.method == "POST":
        get_jenis_surat   = request.POST.get("jenis_surat")
        get_inisial_huruf = request.POST.get("inisialisai_huruf")

        tambah_jenis_surat = DbJenisSurat(
            jenis_surat  = get_jenis_surat,
            inisial_nama = get_inisial_huruf
        )

        tambah_jenis_surat.save()
        return redirect("jenis_surat")
    
@login_required(login_url="/accounts/login/")
def edit_jenis_surat(request , id_jenis_surat ):
    edit_jenis_surat = get_object_or_404(DbJenisSurat, pk = id_jenis_surat)
    
    if request.method == 'POST':
        get_jenis_surat   = request.POST.get("jenis_surat")
        get_inisial_huruf = request.POST.get("inisialisai_huruf")

        edit_jenis_surat = DbJenisSurat(
            id           = id_jenis_surat,
            jenis_surat  = get_jenis_surat,
            inisial_nama = get_inisial_huruf
        )

        edit_jenis_surat.save()
        return redirect('jenis_surat')
        
@login_required(login_url="/accounts/login/")
def delete_jenis_surat(request , id_jenis_surat):
    delete_jenis_surat = get_object_or_404(DbJenisSurat, pk = id_jenis_surat)

    if request.method == 'POST':
        delete_jenis_surat.delete()

        return redirect('jenis_surat')
    
##########################################################
@login_required(login_url="/accounts/login/")
def derajat_surat(request):
    derajat_surat_data = DbDerajatSurat.objects.all().values()

    context = {
        "page_title"    : "DERAJAT SURAT", 
        'derajat_surat' :  derajat_surat_data
        }

    return render(request, "pages/setting/derajat_surat/index.html", context)

@login_required(login_url="/accounts/login/")
def tambah_derajat_surat(request):

    if request.method == "POST":
        get_derajat_surat = request.POST.get("derajat_surat")

        tambah_derajat_surat = DbDerajatSurat(
            dejarat_surat    = get_derajat_surat,
        )

        tambah_derajat_surat.save()
        return redirect("derajat_surat")
    
@login_required(login_url="/accounts/login/")
def edit_derajat_surat(request , id_derajat_surat ):
    edit_derajat_surat = get_object_or_404(DbDerajatSurat, pk = id_derajat_surat)
    
    if request.method == 'POST':
        get_edit_derajat_surat        = request.POST.get('edit_derajat_surat')
            
        edit_derajat_surat = DbDerajatSurat(
                id               = id_derajat_surat,
                dejarat_surat    = get_edit_derajat_surat,        
        )
            
        edit_derajat_surat.save()
        return redirect('derajat_surat')
    
@login_required(login_url="/accounts/login/")
def delete_derajat_surat(request , id_derajat_surat):
    delete_derajat_surat = get_object_or_404(DbDerajatSurat, pk = id_derajat_surat)

    if request.method == 'POST':
        delete_derajat_surat.delete()

        return redirect('derajat_surat')
        
