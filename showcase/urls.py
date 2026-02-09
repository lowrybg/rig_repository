from django.urls import path

from showcase.views import RigListView, RigCreateView, RigUpdateView, RigDeleteView

urlpatterns = [
    path('catalog/', RigListView.as_view(),name='catalog'),
    path('create/', RigCreateView.as_view(),name='create_rig'),
    path('edit/<int:pk>/', RigUpdateView.as_view(),name='edit_rig'),
    path('delete/<int:pk>/', RigDeleteView.as_view(),name='delete_rig'),
]