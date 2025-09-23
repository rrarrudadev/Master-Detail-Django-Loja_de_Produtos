from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.tecnologia, name='tecnologia'),
    path('', views.vestuario, name='vestuario'),
    path('<int:pk>/', views.detalhe, name='detalhe'),
]