from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('soldiers/', views.soldiers, name='soldiers'),
    path('soldiers/<int:soldier_id>', views.soldier, name='soldier'),
    path('weapons/', views.WeaponListView.as_view(), name='weapons'),
    path('weapons/<int:pk>', views.WeaponDetailView.as_view(), name='weapon-detail'),
    path('search/', views.search, name='search'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('weaponunits/', views.WeaponUnitListView.as_view(), name='weapon_unit'),
    ]