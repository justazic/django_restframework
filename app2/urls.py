from .views import CarList, CarUpdate, SearchView #,DeleteView, UpdateView,DetailView,CreateView
from django.urls import path

urlpatterns = [
    path('list/', CarList.as_view(), name='car-list'),
    path('update/<int:pk>/', CarUpdate.as_view(), name='car-update'),
    path('search/', SearchView.as_view(), name='car-search'),
    # path('detail/<int:pk>/', DetailView.as_view(), name='car-detail'),
    # path('create/', CreateView.as_view(), name='car-create'),
    
    # path('delete/<int:pk>/', DeleteView.as_view(), name='car-delete'),
]