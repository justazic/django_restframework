from .views import CarsListView, CarsDetailView, CarsCreateView,CarsUpdateView, CarsListCreateView, CarsUpdateDetailDeleteView
from django.urls import path

urlpatterns = [
    path('list/', CarsListView.as_view()),
    path('detail/<int:pk>/', CarsDetailView.as_view()),
    path('create/', CarsCreateView.as_view()),
    path('update/<int:pk>/', CarsUpdateView.as_view()),
    path('list-create/', CarsListCreateView.as_view()),
    path('update-read-delete/<int:pk>/', CarsUpdateDetailDeleteView.as_view()),
]