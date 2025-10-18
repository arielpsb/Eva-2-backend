from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'main'),
    path('categoria/<str:categoria>/', views.producto_cat, name='categoria'),
    path('producto/<int:id>/', views.producto_detalle, name='detalle'),
]