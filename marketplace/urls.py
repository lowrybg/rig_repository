from django.urls import path
from .views import CreateListingView, MarketplaceView

urlpatterns = [
    path('', MarketplaceView.as_view(), name='marketplace_home'),
    path('sell/', CreateListingView.as_view(), name='create_listing'),
]