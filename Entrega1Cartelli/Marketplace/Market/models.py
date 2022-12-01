from django.db import models

class Vendedor(models.Model):
    nombre_ven= models.CharField(max_length=40)
    id_vendedor=models.IntegerField()
    precio=models.IntegerField()


class Producto(models.Model):
    nombre_pro=models.CharField(max_length=40)
    id_producto=models.IntegerField()
    categoria=models.CharField(max_length=40)


class Categoria (models.Model):
    nombre_cate=models.CharField(max_length=40)
    caracteristicas=models.CharField(max_length=40)
    cuotas=models.BooleanField()

