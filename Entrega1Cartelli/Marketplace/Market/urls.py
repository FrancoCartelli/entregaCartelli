from django.urls import path
from Market import views


urlpatterns = [
   path('', views.inicio,name="Inicio"),
   path('productoApi/', views.MarketPApi),
   path('categoriaApi/', views.MarketCapi),
   path('vendedoresApi/', views.MarketVApi),
   
   path('vendedores/', views.ven_v ,name="vendedores"),
   path('productos/', views.prod_v , name="productos"),
   path('categoria/', views.cat_v , name="categoria"),



]
