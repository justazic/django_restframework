from .views import DeleteView, UpdateView,ListView,DetailView,CreateView
from django.urls import path

urlpatterns = [
    path('list/', ListView.as_view(), name='car-list'),
    path('detail/<int:pk>/', DetailView.as_view(), name='car-detail'),
    path('create/', CreateView.as_view(), name='car-create'),
    path('update/<int:pk>/', UpdateView.as_view(), name='car-update'),
    path('delete/<int:pk>/', DeleteView.as_view(), name='car-delete'),
]