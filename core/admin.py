from django.contrib import admin

from . import models
# Register your models here.
class BarangAdmin(admin.ModelAdmin):
    list_display    = ['nama_barang', 'jumlah_barang', 'tanggal_barang']
    search_fields   = ['nama_barang']
    list_filter     = ['tanggal_barang']

admin.site.register(models.Barang, BarangAdmin)