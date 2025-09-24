from django.urls import path
from . import views

app_name = 'app:index'

urlpatterns = [
    path('', views.index, name='index'),
    path('tecnologia/', views.tecnologia, name='tecnologia'),
    path('vestuario/', views.vestuario, name='vestuario'),
    path('detalhe/<int:pk>/', views.detalhe, name='detalhe'),
]