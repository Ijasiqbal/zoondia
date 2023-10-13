from django.urls import path
from .views import CustomLoginView ,register,dashboard

urlpatterns = [
    path('login/', CustomLoginView.as_view(),name='login'),
    path('register/', register,name='register'),
    path('dashboard/', dashboard,name='dashboard'),
]
