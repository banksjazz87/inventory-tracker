"""
URL configuration for inventory_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('menu-items/', views.MenuItemListView.as_view(), name='menu-item-list'),
    path('purchases/', views.PurchaseListView.as_view(), name='purchase-list'),

    path('ingredients/', views.InventoryItemListView.as_view(), name='ingredient-list'),
    path('ingredients/create_form/', views.AddIngredientView.as_view(), name='add-ingredient'),
    path('ingredients/success/', views.IngredientSuccess.as_view(), name="ingredient-success"),
    path('ingredients/edit/<int:pk>', views.EditIngredientView.as_view(), name="ingredient-edit"),
    path('ingredients/delete/<int:pk>', views.DeleteIngredientView.as_view(), name="ingredient-delete"),
]
