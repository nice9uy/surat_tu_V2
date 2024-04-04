from django.urls import path
from . import views

urlpatterns = [
   path('surat_masuk/', views.surat_masuk_admin, name="surat_masuk_admin"),
#    path('logout/', views.logout_view, name="logout"),
]