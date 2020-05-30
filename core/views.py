from django.shortcuts import (
    render,
    get_object_or_404,
)
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy

from .models import Barang
from .forms import BarangForm
# Create your views here.

class Create(CreateView):
    template_name       = 'core/create.html'
    form_class          = BarangForm

class Update(UpdateView):
    template_name       = 'core/create.html'
    form_class          = BarangForm

    def get_object(self):
        id_             = self.kwargs.get('id')
        return get_object_or_404(Barang, id=id_)

class Delete(DeleteView):
    template_name       = 'core/delete.html'
    success_url         = reverse_lazy('home')
    def get_object(self):
        id_             = self.kwargs.get('id')
        return get_object_or_404(Barang, id=id_)