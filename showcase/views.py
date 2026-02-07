from django.views.generic import ListView
from .models import Rig

class RigListView(ListView):
    model = Rig
    template_name = 'showcase/catalog.html'
    context_object_name = 'rigs'
