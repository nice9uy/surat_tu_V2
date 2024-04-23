from django.urls import path
from . import views

urlpatterns = [
   path('surat_masuk/', views.surat_masuk, name="surat_masuk"),
    
   path('surat_masuk/set_tu/', views.set_tu, name="set_tu"),


   path('surat_masuk/generate_no_agenda/', views.generate_no_agenda, name="generate_no_agenda"),
   path('surat_masuk/tambah_surat_masuk/', views.tambah_surat_masuk, name="tambah_surat_masuk"),
   path('surat_masuk/delete_no_agenda_temp/', views.delete_no_agenda_temp, name="delete_no_agenda_temp"),

   path('surat_masuk/edit_surat_masuk/<int:id_edit_surat_masuk>/', views.edit_surat_masuk, name='edit_surat_masuk'),
   path('surat_masuk/delete_surat_masuk/<int:id_delete_surat_masuk>/', views.delete_surat_masuk, name='delete_surat_masuk'),

   path('surat_masuk/kabaranahan/<int:getIDdisosisi_kabaranahan>', views.kabaranahan, name='kabaranahan'),
   path('surat_masuk/sekretariat/<int:getIDdisosisi_sekretariat>', views.sekretariat, name='sekretariat'),
   path('surat_masuk/bagum/<int:getIDdisosisi_bagum>', views.bagum, name='bagum'),


]