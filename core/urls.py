from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Familias
    path('familias/', views.FamiliaListView.as_view(), name='familia_list'),
    path('familias/nueva/', views.FamiliaCreateView.as_view(), name='familia_create'),
    path('familias/<int:pk>/', views.FamiliaDetailView.as_view(), name='familia_detail'),
    path('familias/<int:pk>/editar/', views.FamiliaUpdateView.as_view(), name='familia_update'),
    path('familias/<int:pk>/eliminar/', views.FamiliaDeleteView.as_view(), name='familia_delete'),

    # Tipos de ayuda
    path('tipos/', views.TipoListView.as_view(), name='tipo_list'),
    path('tipos/nuevo/', views.TipoCreateView.as_view(), name='tipo_create'),
    path('tipos/<int:pk>/', views.TipoDetailView.as_view(), name='tipo_detail'),
    path('tipos/<int:pk>/editar/', views.TipoUpdateView.as_view(), name='tipo_update'),
    path('tipos/<int:pk>/eliminar/', views.TipoDeleteView.as_view(), name='tipo_delete'),

    # Voluntarios
    path('voluntarios/', views.VoluntarioListView.as_view(), name='voluntario_list'),
    path('voluntarios/nuevo/', views.VoluntarioCreateView.as_view(), name='voluntario_create'),
    path('voluntarios/<int:pk>/', views.VoluntarioDetailView.as_view(), name='voluntario_detail'),
    path('voluntarios/<int:pk>/editar/', views.VoluntarioUpdateView.as_view(), name='voluntario_update'),
    path('voluntarios/<int:pk>/eliminar/', views.VoluntarioDeleteView.as_view(), name='voluntario_delete'),

    # Entregas
    path('entregas/', views.EntregaListView.as_view(), name='entrega_list'),
    path('entregas/nueva/', views.EntregaCreateView.as_view(), name='entrega_create'),
    path('entregas/<int:pk>/', views.EntregaDetailView.as_view(), name='entrega_detail'),
    path('entregas/<int:pk>/editar/', views.EntregaUpdateView.as_view(), name='entrega_update'),
    path('entregas/<int:pk>/eliminar/', views.EntregaDeleteView.as_view(), name='entrega_delete'),

    # Seguimientos
    path('seguimientos/', views.SeguimientoListView.as_view(), name='seguimiento_list'),
    path('seguimientos/nuevo/', views.SeguimientoCreateView.as_view(), name='seguimiento_create'),
    path('seguimientos/<int:pk>/', views.SeguimientoDetailView.as_view(), name='seguimiento_detail'),
    path('seguimientos/<int:pk>/editar/', views.SeguimientoUpdateView.as_view(), name='seguimiento_update'),
    path('seguimientos/<int:pk>/eliminar/', views.SeguimientoDeleteView.as_view(), name='seguimiento_delete'),
]
