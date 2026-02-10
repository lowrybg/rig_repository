from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from .forms import RigForm
from .models import Rig

class RigListView(ListView):
    model = Rig
    template_name = 'showcase/catalog.html'
    context_object_name = 'rigs'

class RigCreateView(CreateView):
    model = Rig
    form_class = RigForm
    template_name = 'showcase/create_rig.html'
    success_url = reverse_lazy('catalog')

class RigUpdateView(UpdateView):
    model = Rig
    form_class = RigForm
    template_name = 'showcase/edit_rig.html'
    success_url = reverse_lazy('catalog')

class RigDeleteView(DeleteView):
    model = Rig
    template_name = 'showcase/delete_rig.html'
    success_url = reverse_lazy('catalog')

class RigDetailView(DetailView):
    model = Rig
    template_name = 'showcase/detail_rig.html'
    context_object_name = 'rig'

