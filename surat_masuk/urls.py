from django.urls import path
from . import views

urlpatterns = [
   path('surat_masuk/', views.surat_masuk, name="surat_masuk"),
#    path('logout/', views.logout_view, name="logout"),
]