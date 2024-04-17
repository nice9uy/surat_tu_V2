from datetime import date
from django.shortcuts import redirect, render
from setting.models import DbJenisSurat,DbDerajatSurat,DbKlasifikasi
from surat_masuk.models import DbSurat, TempNoAgenda


# Create your views here.
def surat_masuk(request):

    if request.user.is_authenticated:

        if request.user.groups.filter(name="ADMIN_TU").exists():

            jenis_surat_data     = list(DbJenisSurat.objects.all().values_list('jenis_surat' , flat=True))

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
    username       = request.user

    print(username)

    no         = 1
    hari_ini   = date.today()
    bulan_ini  = date.today().month
    tahun_ini  = date.today().year

    print(type(tahun_ini))
    # tahun_ini  = 2025

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
        get_data                       = DbSurat.objects.filter(no_agenda__icontains = jenis_surat , id_jenis_surat = id_surat , no_agenda__contains = tahun_ini).last()
     
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
            # get_thn                        = int(x_data[3])
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
                
    return render(request, "pages/surat_masuk/admin/pages_tambah_surat_masuk.html")

     
        #         x_data                         = get_data.no_agenda.split("/")
        #         get_thn                        = int(x_data[3])
        #         no_urut_data                   = int(x_data[1])
        #         no_urut                        = no_urut_data + 1
        #         format_no_agenda_save          = f"{jenis_surat}/{no_urut}/{bulan}/{tahun_ini}"
                
        #         ###########################################################################################
        #         get_datax                      = DbSurat.objects.filter(no_agenda__contains = tahun_ini).count()
        #         get_datax_inisial_agenda       = DbSurat.objects.filter(no_agenda__contains = jenis_surat).count()
        #         ############################################################################################  
        #     except:
        #           pass  

        # except:

        #     if get_data == None:
            
        #         save_to_no_agenda = TempNoAgenda(   
        #                 username     =  user,
        #                 no_agenda    =  format_no_agenda,
        #                 jenis_surat  =  str(get_jenis_surat),
        #                 tgl_agenda   =  hari_ini
        #             )   
        #         save_to_no_agenda.save()
        #         # return redirect('tambah_surat_masuk')     
    

                  
        # try:
           
        #     print(x_data)


        #     # print(get_datax)

        #     if get_datax_inisial_agenda == 0 or get_datax == 0:
        #         save_to_no_agenda = TempNoAgenda(   
        #             username     =  user,
        #             no_agenda    =  format_no_agenda,
        #             jenis_surat  =  str(get_jenis_surat),
        #             tgl_agenda   =  hari_ini
        #         )   
        #         save_to_no_agenda.save()
        #         return redirect('tambah_surat_masuk')
        #     elif get_thn != tahun_ini :   
        #         format_no_agenda_final               = f"{jenis_surat}/{no}/{bulan}/{tahun_ini}"
        #         save_to_no_agenda = TempNoAgenda(  
        #             username                         =  user,
        #             no_agenda                        =  format_no_agenda_final,
        #             jenis_surat                      =  str(get_jenis_surat),
        #             tgl_agenda                       =  hari_ini
        #         )
        #         save_to_no_agenda.save()
        #         return redirect('tambah_surat_masuk')
        #     else:            
        #         save_to_no_agenda = TempNoAgenda(   
        #             username                         =  user,
        #             no_agenda                        =  format_no_agenda_save,
        #             jenis_surat                      =  str(get_jenis_surat),
        #             tgl_agenda                       =  hari_ini
        #         )
        #         save_to_no_agenda.save()
        #         return redirect('tambah_surat_masuk')
        # except:
        #     try:
        #         save_to_no_agenda    = TempNoAgenda(   
        #                 username                         =  user,
        #                 no_agenda                        =  format_no_agenda,
        #                 jenis_surat                      =  str(get_jenis_surat),
        #                 tgl_agenda                       =  hari_ini
        #             )
        #         save_to_no_agenda.save()
        #         return redirect('tambah_surat_masuk')
        #     except:
        #         return redirect('surat_masuk')


    

def submit_tambah_surat_masuk(request):
    return render(request, "pages/surat_masuk/admin/pages_tambah_surat_masuk.html")

