from datetime import date
from django.shortcuts import redirect, render, get_object_or_404
from setting.models import DbJenisSurat,DbDerajatSurat,DbKlasifikasi
from surat_masuk.models import DbSurat, TempNoAgenda
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.http import HttpResponse
from weasyprint import HTML
import string
import random
import secrets

########### DISPOSISI ################################

@login_required(login_url="/accounts/login/")
def kabaranahan(request, getIDdisosisi_kabaranahan ):
    getIDdisposisi = get_object_or_404(DbSurat, pk = getIDdisosisi_kabaranahan)
    template = get_template('pdf_disposisi/TU_SET/kabaranahan.html')

    no_agenda         = getIDdisposisi.no_agenda
    tgl_agenda        = getIDdisposisi.tgl_agenda
    surat_dari        = getIDdisposisi.surat_dari
    no_surat          = getIDdisposisi.no_surat
    tgl_surat         = getIDdisposisi.tgl_surat
    klasifikasi       = getIDdisposisi.klasifikasi
    derajat           = getIDdisposisi.derajat_surat

    html_content = template.render({
        'no_agenda'       : no_agenda,
        'tgl_agenda'      : tgl_agenda,
        'surat_dari'      : surat_dari,
        'no_surat'        : no_surat,
        'tgl_surat'       : tgl_surat,
        'klasifikasi'     : klasifikasi,
        'derajat'         : derajat
    })

    pdf_file = HTML(string=html_content).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Kabaranahan - Disposisi"'
    return response

@login_required(login_url="/accounts/login/")
def sekretariat(request, getIDdisosisi_sekretariat):
    getIDdisposisi = get_object_or_404(DbSurat, pk = getIDdisosisi_sekretariat)
    template = get_template('pdf_disposisi/TU_SET/sekretariat.html')


    no_agenda         = getIDdisposisi.no_agenda
    tgl_agenda        = getIDdisposisi.tgl_agenda
    surat_dari        = getIDdisposisi.surat_dari
    no_surat          = getIDdisposisi.no_surat
    tgl_surat         = getIDdisposisi.tgl_surat
    klasifikasi       = getIDdisposisi.klasifikasi
    derajat           = getIDdisposisi.derajat_surat


    html_content = template.render({
        'no_agenda'       : no_agenda,
        'tgl_agenda'      : tgl_agenda,
        'surat_dari'      : surat_dari,
        'no_surat'        : no_surat,
        'tgl_surat'       : tgl_surat,
        'klasifikasi'     : klasifikasi,
        'derajat'         : derajat
    })

    pdf_file = HTML(string=html_content).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Sekretariat - Disposisi"'
    return response

@login_required(login_url="/accounts/login/")
def bagum(request , getIDdisosisi_bagum):
    getIDdisposisi = get_object_or_404(DbSurat, pk = getIDdisosisi_bagum)
    template = get_template('pdf_disposisi/TU_SET/bagum.html')

    no_agenda             = getIDdisposisi.no_agenda
    tgl_agenda            = getIDdisposisi.tgl_agenda
    surat_dari            = getIDdisposisi.surat_dari
    no_surat              = getIDdisposisi.no_surat
    tgl_surat             = getIDdisposisi.tgl_surat
    klasifikasi           = getIDdisposisi.klasifikasi
    derajat               = getIDdisposisi.derajat_surat

    html_content = template.render({
        'no_agenda'       : no_agenda,
        'tgl_agenda'      : tgl_agenda,
        'surat_dari'      : surat_dari,
        'no_surat'        : no_surat,
        'tgl_surat'       : tgl_surat,
        'klasifikasi'     : klasifikasi,
        'derajat'         : derajat
    })

    pdf_file = HTML(string=html_content).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Bagian Umum - Disposisi"'
    return response

#######################################################################################



@login_required(login_url="/accounts/login/")
def surat_masuk(request):
    
    if request.user.is_authenticated:

        if request.user.groups.filter(name="SET_TU").exists():

            kode_keamanan        = ''.join(secrets.choice(string.ascii_letters + string.digits)for i in range(20))

            jenis_surat_data     = list(DbJenisSurat.objects.all().values_list('jenis_surat' , flat=True))
            klasifikasi_data     = list(DbKlasifikasi.objects.all().values_list('klasifikasi' , flat=True))
            surat_masuk          = DbSurat.objects.all()

            context = {
                "page_title"    : "SEKRETARIAT - TU",
                'jenis_surat'   : jenis_surat_data,
                'klasifikasi'   : klasifikasi_data,
                'surat_masuk'   :  surat_masuk,
                'kode_keamanan' : kode_keamanan
            }

            return render(request, "pages/surat_masuk/SET_TU/index.html", context )

        elif request.user.groups.filter(name="TU_SET_KASUBBAG").exists():

            return render(request, "pages/dashboard/kasubbag.html")

        elif request.user.groups.filter(name="USER").exists():
            
            return render(request, "pages/dashboard/user.html")

        else:

            context = {"page_title": "SUPER ADMIN"}

            return render(request, "pages/dashboard/super_admin.html", context)

    else:
        pass


@login_required(login_url="/accounts/login/")
def set_tu(request):
     pass


@login_required(login_url="/accounts/login/")
def delete_no_agenda_temp(request):
    user    = request.user

    hapus_temp_no_agenda = TempNoAgenda.objects.filter(username = user)    
    hapus_temp_no_agenda.delete()

    return redirect('surat_masuk')

@login_required(login_url="/accounts/login/")
def generate_no_agenda(request):
    username               = request.user
    user_cek_first         = TempNoAgenda.objects.values_list('id', flat=True).first()
    user_cek_last          = TempNoAgenda.objects.values_list('id', flat=True).last()
    user_cek               = TempNoAgenda.objects.filter(username = username).values_list('username', flat=True).first()
    # print(user_cek)

    if user_cek_first == None :

        no         = 1
        hari_ini   = date.today()
        bulan_ini  = date.today().month
        tahun_ini  = date.today().year

        if bulan_ini == 1:
                bulan = 'I'
        elif bulan_ini == 2:
                bulan = 'II'
        elif bulan_ini == 3:
                bulan = 'III'
        elif bulan_ini == 4:
                bulan = 'IV'
        elif bulan_ini == 5:
                bulan = 'V'
        elif bulan_ini == 6:
                bulan = 'VI'
        elif bulan_ini == 7:
                bulan = 'VII'
        elif bulan_ini == 8:
                bulan = 'VIII'
        elif bulan_ini == 9:
                bulan = 'IX'
        elif bulan_ini == 10:
                bulan = 'X'
        elif bulan_ini == 11:
                bulan = 'XI'
        else:
                bulan = 'XII'

        if request.method == 'POST':
            
            get_jenis_surat                = request.POST.get('jenis_surat_input')
            ##############################################################
            jenis_surat_list               = list(DbJenisSurat.objects.filter(jenis_surat = get_jenis_surat ).values_list('inisial_nama', flat=True))
            id_jenis_surat                 = list(DbJenisSurat.objects.filter(jenis_surat = get_jenis_surat ).values_list('id', flat=True))
            jenis_surat                    = jenis_surat_list[0]
            id_surat                       = id_jenis_surat[0]
            #############################################################
            format_no_agenda               = f"{jenis_surat}/{no}/{bulan}/{tahun_ini}"
            #############################################################
            get_data                       = DbSurat.objects.filter(no_agenda__icontains = jenis_surat , id_jenis_surat = id_surat , no_agenda__endswith = tahun_ini).last()
            
            if  get_data == None:

                save_to_no_agenda = TempNoAgenda(   
                        
                        username     =  username,
                        no_agenda    =  format_no_agenda,
                        jenis_surat  =  str(get_jenis_surat),
                        tgl_agenda   =  hari_ini
                        
                        )   
                save_to_no_agenda.save()
                return redirect('tambah_surat_masuk')
            
            else:

                x_data                         = get_data.no_agenda.split("/")
                no_urut_data                   = int(x_data[1])
                no_urut                        = no_urut_data + 1
                format_no_agenda_save          = f"{jenis_surat}/{no_urut}/{bulan}/{tahun_ini}"

                save_to_no_agenda = TempNoAgenda(   
                        username                         =  username,
                        no_agenda                        =  format_no_agenda_save,
                        jenis_surat                      =  str(get_jenis_surat),
                        tgl_agenda                       =  hari_ini
                    )
                save_to_no_agenda.save()
                return redirect('tambah_surat_masuk')
            
    elif user_cek_first < user_cek_last :
        print("fhgkfaffafaf")
        return redirect('surat_masuk')
    elif username != user_cek :
        print("wkwkwkwkw")
        return redirect('tambah_surat_masuk')    
    else:
        print('qqqqqqqqqq')
        return redirect('surat_masuk')
    
    return render(request, "pages/surat_masuk/SET_TU/pages_tambah_surat_masuk.html")
                
@login_required(login_url="/accounts/login/")
def tambah_surat_masuk(request):
    try:
    
        user                    = request.user
        klasifikasi             = DbKlasifikasi.objects.all().values_list('klasifikasi', flat=True )
        jenis_surat             = DbJenisSurat.objects.all().values_list('jenis_surat', flat=True)
        derajat_surat           = DbDerajatSurat.objects.all().values_list('dejarat_surat', flat=True )
        
        no_agenda_data          = list(TempNoAgenda.objects.filter(username = user).values_list('no_agenda', flat=True ))
        jenis_surat_data        = list(TempNoAgenda.objects.filter(username = user).values_list('jenis_surat', flat=True ))
        tgl_agenda_surat        = list(TempNoAgenda.objects.filter(username = user).values_list('tgl_agenda', flat=True ))
        no_agenda               = no_agenda_data[0]
        jenis_surat_x           = jenis_surat_data[0]
        tgl_agenda              = tgl_agenda_surat[0]

    
        if request.method == 'POST':

                get_jenis_surat       = request.POST.get('jenis_surat')
                get_klasifikasi       = request.POST.get('klasifikasi')
                get_tanggal_agenda    = request.POST.get('tanggal_agenda')
                get_no_agenda         = request.POST.get('no_agenda')

                get_tanggal_surat     = request.POST.get('tanggal_surat')

                get_no_surat          = request.POST.get('no_surat')
                get_surat_dari        = request.POST.get('surat_dari')
                get_derajat_surat     = request.POST.get('derajat_surat')
                get_perihal           = request.POST.get('perihal')
                files_upload          = request.FILES.get('file_name')
                #############################################################################
                id_jenis_surat        = list(DbJenisSurat.objects.filter(jenis_surat = get_jenis_surat ).values_list('id', flat=True))
                id_surat_final        = id_jenis_surat[0]
                ##############################################################################
                tambah_data_surat = DbSurat(

                        username      = user,
                        jenis_surat   = get_jenis_surat,
                        klasifikasi   = get_klasifikasi,
                        tgl_agenda    = get_tanggal_agenda,
                        id_jenis_surat= id_surat_final,
                        no_agenda     = get_no_agenda,

                        tgl_surat     = get_tanggal_surat if get_tanggal_surat else None ,

                        no_surat      = get_no_surat,
                        surat_dari    = get_surat_dari,
                        derajat_surat = get_derajat_surat,
                        perihal       = get_perihal,
                        upload_file   = files_upload
                        
                        )
                
                tambah_data_surat.save()

                hapus_temp_no_agenda = TempNoAgenda.objects.filter(username = user)    
                hapus_temp_no_agenda.delete()

                return redirect('surat_masuk')

        context = {
              
            'page_title'     : 'Tambah Surat',
            'klasifikasi'    : klasifikasi,
            'jenis_surat'    : jenis_surat,
            'derajat_surat'  : derajat_surat,
            'no_agenda'      : no_agenda,
            'jenis_surat'    : jenis_surat_x,
            'hari_ini'       : tgl_agenda       
        }

        return render(request, "pages/surat_masuk/SET_TU/pages_tambah_surat_masuk.html", context)

    except Exception as e:
        print(e)



@login_required(login_url="/accounts/login/")
def edit_surat_masuk(request , id_edit_surat_masuk ):
    username = request.user
    edit_surat_masuk = get_object_or_404(DbSurat, pk = id_edit_surat_masuk)

    
    try:
        if request.method == 'POST':
            get_jenis_surat           = request.POST.get('jenis_surat')
            get_klasifikasi           = request.POST.get('klasifikasi')
            get_tgl_agenda            = request.POST.get('tanggal_agenda')          
            get_no_agenda             = request.POST.get('no_agenda')

            get_tanggal_surat         = request.POST.get('tanggal_surat')

            get_no_surat              = request.POST.get('no_surat')
            get_surat_dari            = request.POST.get('surat_dari')
            get_derajat_surat         = request.POST.get('derajat_surat')
            get_perihal               = request.POST.get('perihal')
            files_upload_data         = request.FILES.get('file_name')

            data_surat =  edit_surat_masuk.upload_file.name

            if  files_upload_data == None:
                files_upload  = data_surat

            else:
                files_upload = files_upload_data
                edit_surat_masuk.upload_file.delete()

            edit_surat_masuk = DbSurat(

                id             = id_edit_surat_masuk,
                username       = str(username),
                jenis_surat    = get_jenis_surat,
                klasifikasi    = get_klasifikasi,
                tgl_agenda     = get_tgl_agenda,
                id_jenis_surat = edit_surat_masuk.id_jenis_surat,
                no_agenda      = get_no_agenda,
                
                tgl_surat      = get_tanggal_surat if get_tanggal_surat else None ,

                no_surat       = get_no_surat,
                surat_dari     = get_surat_dari,
                derajat_surat  = get_derajat_surat,
                perihal        = get_perihal,
                upload_file    = files_upload
                
                )
            
            edit_surat_masuk.save()
            return redirect('surat_masuk')        
    except:
        return redirect('surat_masuk')
    

@login_required(login_url="/accounts/login/")
def delete_surat_masuk(request , id_delete_surat_masuk):
    delete_surat_masuk = get_object_or_404(DbSurat, pk = id_delete_surat_masuk)

    if request.method == 'POST':

        kode_keamanan_1    =  request.POST.get('kode_1')
        kode_keamanan_2    =  request.POST.get('kode_2')

        if kode_keamanan_1 == kode_keamanan_2:

            delete_surat_masuk.upload_file.delete()
            delete_surat_masuk.delete()
            return redirect('surat_masuk')
        else:
            return redirect('surat_masuk')
    
    return render(request,'pages/olah_surat.html')