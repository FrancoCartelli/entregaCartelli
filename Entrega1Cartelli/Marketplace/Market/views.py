from django.shortcuts import render
from django.http import HttpResponse
from Market.models   import Vendedor,Producto,Categoria
from django.core import serializers
from Market.forms import VendedorFormulario,ProductoFormulario,CategoriaFormulario

# Create your views here.


def MarketVApi(request):
    ven_todos=Vendedor.objects.all()
    return HttpResponse(serializers.serialize("json",ven_todos))


def MarketPApi(request):
    prod_todos=Producto.objects.all()
    return HttpResponse(serializers.serialize("json",prod_todos))


def MarketCapi(request):
    cat_todos=Categoria.objects.all()
    return HttpResponse(serializers.serialize("json",cat_todos))





def inicio(request):
    
   return render(request,"MarketTem/inicio.html")








    



def ven_v(request):
    if request.method == "POST":
        miFormulario = VendedorFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            produc = Vendedor(nombre_ven=informacion["nombre_vende"], id_vendedor=informacion["id_vendedor"], precio=informacion["precio"])
            produc.save()
            return render(request, "MarketTem/inicio.html")
    else:
        miFormulario = VendedorFormulario()
    return render(request, "MarketTem/vendedor.html", {"miFormulario": miFormulario})



def prod_v(request):
    if request.method == "POST":
        miFormulario = ProductoFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            produc = Producto(nombre_pro=informacion["nombre_pro"], id_producto=informacion["id_producto"], categoria=informacion["categoria"])
            produc.save()
            return render(request, "MarketTem/inicio.html")
    else:
        miFormulario = ProductoFormulario()
    return render(request, "MarketTem/producto.html", {"miFormulario": miFormulario})


def cat_v(request):
    if request.method == "POST":
        miFormulario = CategoriaFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            produc = Categoria(nombre_cate=informacion["nombre_cate"], caracteristicas=informacion["caracteristicas"], cuotas=informacion["cuotas"])
            produc.save()
            return render(request, "MarketTem/inicio.html")
    else:
        miFormulario = CategoriaFormulario()
    return render(request, "MarketTem/categoria.html", {"miFormulario": miFormulario})





