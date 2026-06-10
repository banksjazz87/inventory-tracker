from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, CreateView, View
from django.views.generic.edit import UpdateView, DeleteView
from urllib.parse import urlencode
from django.urls import reverse_lazy, reverse
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from .forms import *

class HomeView(TemplateView):
   template_name = "main/home.html"



################################################
## MENU ITEM VIEWS ##
################################################
class MenuItemListView(ListView):
    model = MenuItem
    template_name = "menu-items/index.html"
    context_object_name = "items"

class MenuIngredientList(ListView):
    model = RecipeRequirement
    template_name = "menu-items/ingredient_list.html"
    context_name = "ingredients"

    def get_queryset(self):
        fk_id = self.kwargs.get('pk')
        return RecipeRequirement.objects.filter(menu_item=fk_id)
    
class MenuSuccess(TemplateView):
    template_name = "menu-items/success.html"
    
class AddMenuItem(TemplateView):
    template_name = "menu-items/add_menu_item_form.html"

    def get(self, request, *args, **kwargs):
        menu_form = AddMenuItemForm(prefix="menu")
        recipe_form = AddRecipeRequirementForm(prefix="recipe")

        return self.render_to_response({
            'menu_form': menu_form,
            'recipe_form': recipe_form
        })

    def post(self, request):
        menu_form = AddMenuItemForm(request.POST)
        recipe_form = AddRecipeRequirementForm(request.POST)

        if menu_form.is_valid() and recipe_form.is_valid():
            menu_instance = menu_form.save()
            recipe_instance = recipe_form.save(commit=False)
            recipe_instance.menu_item = menu_instance
            recipe_instance.save()

            return redirect('menu-success')
        
        return self.render_to_response({
            'menu_form': menu_form,
            'recipe_form': recipe_form
        })




################################################
## PURCHASE VIEWS ##
################################################
class PurchaseListView(TemplateView):
    template_name = "purchases/index.html"

################################################
## INGREDIENT VIEWS ##
################################################
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