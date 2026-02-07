from django.urls import path

from showcase.views import RigListView

urlpatterns = [
    path('catalog/', RigListView.as_view(),name='catalog'),
]