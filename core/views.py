from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Familia, TipoAyuda, Voluntario, Entrega, Seguimiento
from .forms import FamiliaForm, TipoAyudaForm, VoluntarioForm, EntregaForm, SeguimientoForm

def home(request):
    return render(request, 'home.html')

# ---------- FAMILIAS ----------
class FamiliaListView(generic.ListView):
    model = Familia
    template_name = 'familia_list.html'

class FamiliaDetailView(generic.DetailView):
    model = Familia
    template_name = 'familia_detail.html'

class FamiliaCreateView(generic.CreateView):
    model = Familia
    form_class = FamiliaForm
    template_name = 'familia_form.html'
    success_url = reverse_lazy('familia_list')

class FamiliaUpdateView(generic.UpdateView):
    model = Familia
    form_class = FamiliaForm
    template_name = 'familia_form.html'
    success_url = reverse_lazy('familia_list')

class FamiliaDeleteView(generic.DeleteView):
    model = Familia
    template_name = 'familia_confirm_delete.html'
    success_url = reverse_lazy('familia_list')

# ---------- TIPOS DE AYUDA ----------
class TipoListView(generic.ListView):
    model = TipoAyuda
    template_name = 'tipo_list.html'

class TipoDetailView(generic.DetailView):
    model = TipoAyuda
    template_name = 'tipo_detail.html'

class TipoCreateView(generic.CreateView):
    model = TipoAyuda
    form_class = TipoAyudaForm
    template_name = 'tipo_form.html'
    success_url = reverse_lazy('tipo_list')

class TipoUpdateView(generic.UpdateView):
    model = TipoAyuda
    form_class = TipoAyudaForm
    template_name = 'tipo_form.html'
    success_url = reverse_lazy('tipo_list')

class TipoDeleteView(generic.DeleteView):
    model = TipoAyuda
    template_name = 'tipo_confirm_delete.html'
    success_url = reverse_lazy('tipo_list')

# ---------- VOLUNTARIOS ----------
class VoluntarioListView(generic.ListView):
    model = Voluntario
    template_name = 'voluntario_list.html'

class VoluntarioDetailView(generic.DetailView):
    model = Voluntario
    template_name = 'voluntario_detail.html'

class VoluntarioCreateView(generic.CreateView):
    model = Voluntario
    form_class = VoluntarioForm
    template_name = 'voluntario_form.html'
    success_url = reverse_lazy('voluntario_list')

class VoluntarioUpdateView(generic.UpdateView):
    model = Voluntario
    form_class = VoluntarioForm
    template_name = 'voluntario_form.html'
    success_url = reverse_lazy('voluntario_list')

class VoluntarioDeleteView(generic.DeleteView):
    model = Voluntario
    template_name = 'voluntario_confirm_delete.html'
    success_url = reverse_lazy('voluntario_list')

# ---------- ENTREGAS ----------
class EntregaListView(generic.ListView):
    model = Entrega
    template_name = 'entrega_list.html'

class EntregaDetailView(generic.DetailView):
    model = Entrega
    template_name = 'entrega_detail.html'

class EntregaCreateView(generic.CreateView):
    model = Entrega
    form_class = EntregaForm
    template_name = 'entrega_form.html'
    success_url = reverse_lazy('entrega_list')

class EntregaUpdateView(generic.UpdateView):
    model = Entrega
    form_class = EntregaForm
    template_name = 'entrega_form.html'
    success_url = reverse_lazy('entrega_list')

class EntregaDeleteView(generic.DeleteView):
    model = Entrega
    template_name = 'entrega_confirm_delete.html'
    success_url = reverse_lazy('entrega_list')

# ---------- SEGUIMIENTOS ----------
class SeguimientoListView(generic.ListView):
    model = Seguimiento
    template_name = 'seguimiento_list.html'

class SeguimientoDetailView(generic.DetailView):
    model = Seguimiento
    template_name = 'seguimiento_detail.html'

class SeguimientoCreateView(generic.CreateView):
    model = Seguimiento
    form_class = SeguimientoForm
    template_name = 'seguimiento_form.html'
    success_url = reverse_lazy('seguimiento_list')

class SeguimientoUpdateView(generic.UpdateView):
    model = Seguimiento
    form_class = SeguimientoForm
    template_name = 'seguimiento_form.html'
    success_url = reverse_lazy('seguimiento_list')

class SeguimientoDeleteView(generic.DeleteView):
    model = Seguimiento
    template_name = 'seguimiento_confirm_delete.html'
    success_url = reverse_lazy('seguimiento_list')
