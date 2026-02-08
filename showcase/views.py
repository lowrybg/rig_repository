from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

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
