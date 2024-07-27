from django.urls import path
from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<str:url>/', HomeView.as_view(), name='item_view'),
]
