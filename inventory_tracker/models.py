from django.db import models

class Ingredient(models.Model):
    COOKING_UNITS = {
        "tsp": "Teaspoon",
        "tbsp": "Tablespoon",
        "fl oz": "Fluid Ounce",
        "c": "Cup",
        "pt": "Pint",
        "gal": "Gallon",
        "ml": "Milliliter",
        "l": "Liter",
        "g": "Gram",
        "kg": "Kilogram",
        "oz": "Ounce",
        "lb": "Pound",
        "mg": "Milligram",
        "cn": "Can",
        "pkg": "Package",
        "qty": "Quantity"
    }
    name = models.CharField(max_length=250)
    quantity = models.IntegerField()
    unit_name = models.CharField(max_length=5, choices=COOKING_UNITS)
    price_per_unit = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"\n name: {self.name}\n quantity: {self.quantity}\n unit_name: {self.unit_name}\n price_per_unit: {self.price_per_unit}"


class MenuItem(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"\nid: {self.pk} \n name: {self.name}\nprice: {self.price}"


class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"\n menu_item: {self.menu_item} \n ingredient: {self.ingredient} \n quantity: {self.quantity}"


class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField()

    def __str__(self):
        return f"\n menu_item: {self.menu_item}\n time_stamp: {self.time_stamp}"

