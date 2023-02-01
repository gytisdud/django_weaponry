from django.urls import path, include
from . import views
from .views import delete_item, WeaponByAdminDeleteView

urlpatterns = [
    path('', views.index, name='index'),
    path('soldiers/', views.soldiers, name='soldiers'),
    path('soldiers/<int:soldier_id>', views.soldier, name='soldier'),
    path('weapons/', views.WeaponListView.as_view(), name='weapons'),
    path('weapons/<int:pk>', views.WeaponDetailView.as_view(), name='weapon-detail'),
    path('search/', views.search, name='search'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('add/add-weapon/', views.WeaponByAdminCreateView.as_view(), name='add-weapon'),
    path('soldiers/<int:soldier_id>/<uuid:pk>', views.WeaponByAdminDeleteView.as_view(), name='delete-weapon'),
    ]