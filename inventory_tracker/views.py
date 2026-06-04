from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase

class HomeView(TemplateView):
   template_name = "main/home.html"


class MenuItemListView(TemplateView):
    model = MenuItem
    template_name = "menu-items/index.html"
    context_object_name = "items"

class PurchaseListView(TemplateView):
    template_name = "purchases/index.html"

class InventoryItemListView(ListView):
    model = Ingredient
    template_name = "ingredients/index.html"
    context_object_name = "ingredients"