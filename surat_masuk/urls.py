from django.urls import path
from . import views

urlpatterns = [
   path('surat_masuk/', views.surat_masuk, name="surat_masuk"),
   path('surat_masuk/tambah_surat_masuk/', views.tambah_surat_masuk, name="tambah_surat_masuk"),
   path('surat_masuk/submit_tambah_surat_masuk/', views.submit_tambah_surat_masuk, name="submit_tambah_surat_masuk"),

#    path('logout/', views.logout_view, name="logout"),
]