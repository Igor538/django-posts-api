from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('posts', views.PostViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('inicio/', views.inicio, name='inicio'),
    path('inicio/<int:editar_id>/', views.inicio, name='inicio_editar'),
    path('postar/', views.postar, name='postar'),
    path('editar/<int:id>/', views.editar_post, name='editar_post'),
    path('remover/<int:id>/', views.remover_post, name='remover_post'),
]
