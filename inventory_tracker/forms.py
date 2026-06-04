from django import forms
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase

class AddIngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'