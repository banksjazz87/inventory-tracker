from django import forms
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase

################################################
## INGREDIENTS FORMS ##
################################################
class AddIngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'

class EditIngredientForm(forms.ModelForm):
    class Meta: 
        model = Ingredient
        fields = '__all__'

class DeleteIngredientForm(forms.ModelForm):
    class Meta: 
        model = Ingredient
        fields = '__all__'

################################################
## MENU ITEM FORMS ##
################################################
class AddMenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'price']

class AddRecipeRequirementForm(forms.ModelForm):
    class Meta: 
        model = RecipeRequirement
        fields = ['ingredient', 'quantity']