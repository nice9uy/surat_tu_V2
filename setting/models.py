from django.db import models


# Create your models here.
class DbKlasifikasi(models.Model):
    id          = models.AutoField(primary_key=True, unique=True)
    klasifikasi = models.CharField(max_length=30)

    class Meta:
        db_table = "Klasifikasi"

class DbJenisSurat(models.Model):
    id           = models.AutoField(primary_key=True, unique=True)
    jenis_surat  = models.CharField(max_length=30)
    inisial_nama = models.CharField(max_length=30)

    class Meta:
        db_table = "JenisSurat"

class DbDerajatSurat(models.Model):
    id            = models.AutoField(primary_key=True, unique=True)
    dejarat_surat = models.CharField(max_length=30)

    class Meta:
        db_table = "DbDerajatSurat"