from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from urllib.parse import urlencode
from django.urls import reverse_lazy, reverse
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from .forms import AddIngredientForm

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

class AddIngredientView(CreateView):
    model = Ingredient
    template_name = "ingredients/create_form.html"
    form_class = AddIngredientForm
    success_url = "ingredients/success.html"
    
    def get_success_url(self):
        base_url = reverse('ingredient-success')
        query_data = {
            'name': self.object.name
        }

        return f"{base_url}?{urlencode(query_data)}"
    
    
class EditIngredientView(UpdateView):
    model = Ingredient
    template_name = "ingredients/edit.html"
    success_url = "ingredients/success.html"
    fields = "__all__"

    def get_success_url(self):
        base_url = reverse('ingredient-success')
        query_data = {
            'name': self.object.name,
            'method': 'updated'
        }

        return f"{base_url}?{urlencode(query_data)}"

class DeleteIngredientView(DeleteView):
    model = Ingredient
    template_name = "ingredients/delete.html"
    success_url = "ingredients/success.html"
    fields = "__all__"

    def get_success_url(self):
        base_url = reverse('ingredient-success')
        query_data = {
            'name': self.object.name,
            'method': 'deleted'
        }

        return f"{base_url}?{urlencode(query_data)}"


class IngredientSuccess(TemplateView):
    model = Ingredient
    template_name = "ingredients/success.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submitted_data'] = self.request.GET

        return context