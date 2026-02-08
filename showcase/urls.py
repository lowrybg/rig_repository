from django.urls import path

from showcase.views import RigListView, RigCreateView

urlpatterns = [
    path('catalog/', RigListView.as_view(),name='catalog'),
    path('create/', RigCreateView.as_view(),name='create_rig'),
]