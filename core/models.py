from django.db import models
from django.urls import reverse

# Create your models here.
class Barang(models.Model):
    gambar_barang   = models.ImageField(upload_to='gambar/', null=True, blank=False)
    nama_barang     = models.CharField(max_length=100, null=False, blank=False)
    jumlah_barang   = models.PositiveIntegerField(null=False, blank=False)
    tanggal_barang  = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nama_barang
    
    def get_absolute_url(self):
        return reverse('home')