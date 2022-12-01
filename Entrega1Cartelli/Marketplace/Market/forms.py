from django import forms



class VendedorFormulario(forms.Form):
    nombre_vende=forms.CharField(max_length=40)
    id_vendedor=forms.IntegerField()
    precio=forms.IntegerField()

class ProductoFormulario(forms.Form):
    nombre_pro=forms.CharField(max_length=40)
    id_producto=forms.IntegerField()
    categoria=forms.CharField(max_length=40)

class CategoriaFormulario(forms.Form):
    nombre_cate=forms.CharField(max_length=40)
    caracteristicas=forms.CharField(max_length=40)
    cuotas=forms.BooleanField()