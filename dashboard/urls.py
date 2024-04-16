from django.urls import path
from . import views

urlpatterns = [
   path('', views.dashboard, name="dashboard"),
   # path('setting_surat/', views.setting_surat, name="setting_surat"),
]

