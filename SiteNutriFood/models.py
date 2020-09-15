from django.db import models

class produits ( models.model):
    ingrédients = models.CharField(max_length=200)