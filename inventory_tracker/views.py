from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
   template_name = "main/home.html"


class MenuItemListView(TemplateView):
    template_name = "menu-items/index.html"

class PurchaseListView(TemplateView):
    template_name = "purchases/index.html"

class InventoryItemListView(TemplateView):
    template_name = "ingredients/index.html"