from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from marketplace.forms import ListingForm
from marketplace.models import Listing


class CreateListingView(LoginRequiredMixin, CreateView):
    model = Listing
    form_class = ListingForm
    template_name = 'marketplace/create_listing.html'

    success_url = reverse_lazy('marketplace_home')

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)

class MarketplaceView(ListView):
    model = Listing
    template_name = 'marketplace/listing_list.html'
    context_object_name = 'listings'
    ordering = ['-created_at']

