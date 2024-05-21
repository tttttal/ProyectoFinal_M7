from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_libros, name='lista_libros'),
    path('crear/', views.crear_libro, name='crear_libro'),
    path('<int:libro_id>/', views.ver_libro, name='ver_libro'),
    path('<int:libro_id>/actualizar/', views.actualizar_libro, name='actualizar_libro'),
    path('<int:libro_id>/borrar/', views.borrar_libro, name='borrar_libro'),
]
