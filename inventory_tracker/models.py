from django.db import models

class Ingredients(models.Model):
    name = models.CharField(max_length=250)
    quantity = models.IntegerField()
    unit_name = models.CharField(max_length=75)
    price_per_unit = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"\n name: {self.name}\n quantity: {self.quantity}\n unit_name: {self.unit_name}\n price_per_unit: {self.price_per_unit}"


class Menu_Items(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    #Pass in the name of the of the ingredient as a comma separated list.
    ingredients = models.TextField()

    def __str__(self):
        return f"\n name: {self.name}\nprice: {self.price}\n ingredients: {self.ingredients}"

class Purchases(models.Model):
    menu_item = models.ForeignKey(Menu_Items, on_delete=models.CASCADE)
    quantity_sold = models.IntegerField()
    purchase_time = models.DateTimeField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"\n menu_item: {self.menu_item}\n quantity_sold: {self.quantity_sold}\n purchase_time: {self.purchase_time}\n total: {self.total}"

