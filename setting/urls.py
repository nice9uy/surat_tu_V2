from django.urls import path
from . import views

urlpatterns = [
   path('klasifkasi/', views.klasifkasi, name="klasifkasi"),
   
   path('edit_klasifikasi/<int:id_klasifikasi>/', views.edit_klasifikasi, name='edit_klasifikasi'),
   path('delete_klasifikasi/<int:id_klasifikasi>/', views.delete_klasifikasi, name='delete_klasifikasi'),

   path('jenis_surat/', views.jenis_surat, name="jenis_surat"),
   path('tambah_jenis_surat/', views.tambah_jenis_surat, name="tambah_jenis_surat"),
   path('edit_jenis_surat/<int:id_jenis_surat>/', views.edit_jenis_surat, name='edit_jenis_surat'),
   path('delete_jenis_surat/<int:id_jenis_surat>/', views.delete_jenis_surat, name='delete_jenis_surat'),

   path('derajat_surat/', views.derajat_surat, name="derajat_surat"),
   path('tambah_derajat_surat/', views.tambah_derajat_surat, name="tambah_derajat_surat"),
]

