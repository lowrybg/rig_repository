from django.urls import path
from .views import CreateListingView

urlpatterns = [

    path('sell/', CreateListingView.as_view(), name='create_listing'),
]