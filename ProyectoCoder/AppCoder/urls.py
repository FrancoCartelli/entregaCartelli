from django.urls import path
from AppCoder import views


urlpatterns = [
    path('cursos/', views.cursos,name="cursos"),
    path('profesores/', views.profesores),
    path('', views.inicio,name="Inicio"),
    path('cursosApi/', views.cursosApi),
    path('busquedacurso/', views.buscarcurso,name="buscar"),
    path('buscar/', views.buscar),
    path('leerCurso/', views.leer_cursos),
    path('crearCurso/', views.crear_cursos),
    path('editarCurso/', views.editar_cursos),
    path('EliminarCurso/', views.eliminar_curso),
    path('curso/list', views.CursoList.as_view(),name="list"),
    path('curso/create', views.CursoCreate.as_view() , name="new"),
    path('curso/edit/<pk>', views.CursoEdit.as_view() , name="Edit"),
    path('curso/detail/<pk>', views.CursoDetalle.as_view() , name="Detail"),
    path('curso/delete/<pk>', views.CursoDelete.as_view() , name="Delete"),

]
