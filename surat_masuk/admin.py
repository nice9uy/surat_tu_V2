from django.contrib import admin

# Register your models here.
from .models import DbSurat
from .models import DisposisiDb
from .models import TempNoAgenda


class ListDbSurat(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "jenis_surat",
        "klasifikasi",
        "tgl_agenda",
        "id_jenis_surat",
        "no_agenda",
        "tgl_surat",
        "no_surat",
        "surat_dari",
        "perihal",
        "derajat_surat",
        "upload_file",
    )


class ListDisposisiDb(admin.ModelAdmin):
    list_display = (
        "no_surat",
        "no_surat_id",
        "id",
        "username",
        "disposisi",
        "tgl_disposisi",
        "no_agenda",
        "catatan",
        "upload_file_disposisi",
    )


class ListTempNoAgenda(admin.ModelAdmin):
    list_display = ("no_agenda", "jenis_surat")


admin.site.site_header = "Admin ARSIP TU SETBARANAHAN"
admin.site.index_title = "SEMUA DATABASE ARSIP"


admin.site.register(DbSurat, ListDbSurat)
admin.site.register(DisposisiDb, ListDisposisiDb)
admin.site.register(TempNoAgenda, ListTempNoAgenda)
