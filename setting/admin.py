from django.contrib import admin

# Register your models here.
from .models import DbKlasifikasi
from .models import DbJenisSurat
from .models import DbDerajatSurat

class ListKlasifikasi(admin.ModelAdmin):
    list_display = ('id','klasifikasi')

class ListDbJenisSurat(admin.ModelAdmin):
    list_display = ('id','jenis_surat','inisial_nama')

class ListDbDerajatSurat(admin.ModelAdmin):
    list_display = ('id','dejarat_surat')


admin.site.register(DbKlasifikasi, ListKlasifikasi)
admin.site.register(DbJenisSurat , ListDbJenisSurat)
admin.site.register(DbDerajatSurat , ListDbDerajatSurat)