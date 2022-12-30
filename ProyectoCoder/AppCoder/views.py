from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models   import Curso
from django.core import serializers
from AppCoder.forms import CursoFormulario

def cursos(request):
    if request.method == "POST":
        miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"], numero_dia=informacion["numero_dia"])
            curso.save()
            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = CursoFormulario()
    return render(request, "AppCoder/cursos.html", {"miFormulario": miFormulario})


def profesores(request):
    return HttpResponse("Vista de profesores")

def inicio(request):
    return render(request,"AppCoder/inicio.html")




def cursosApi(request):
    cursos_todos=Curso.objects.all()
    return HttpResponse(serializers.serialize("json",cursos_todos))




def buscarcurso(request):
    return render(request,"AppCoder/busquedaCurso.html")

def buscar(request):
    camada_views = request.GET['camada']
    cursos_todos=Curso.objects.filter(camada=camada_views )
    return render(request,"AppCoder/resultadoCurso.html",{"camada":camada_views ,"cursos":cursos_todos})


        


def leer_cursos(request):
    cursos_all=Curso.objects.all()
    return HttpResponse (serializers.serialize("json",cursos_all))

def crear_cursos(request): 
    curso=Curso(nombre="cursoTest", camada=199, numero_dia=19)
    curso.save
    return HttpResponse (f"Curso {curso.nombre} ha sido creado")

def editar_cursos(request):
    nombre_consulta= "cursoTest"
    Curso.objects.filter(nombre=nombre_consulta).update(nombre="nombrenuevocursoTest")
    return HttpResponse (f"Curso {nombre_consulta} ha sido actualizado") 

    
def eliminar_curso(request):
    nombre_nuevo='NombrenuevoCursoTest'
    curso = Curso.objects.get(nombre=nombre_nuevo)
    curso.delete()
    return HttpResponse(f'Curso {nombre_nuevo} ha sido eliminado')



from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView



class CursoList(ListView):
    model = Curso
    template = 'AppCoder/curso_list.html'



class CursoCreate(CreateView):
    model = Curso
    fields="__all__"
    success_url="/AppCoder/curso/list"



class CursoDelete(DeleteView):
    model = Curso
    success_url="/AppCoder/curso/list"


class CursoEdit(UpdateView):
    model = Curso
    fields="__all__"
    success_url="/AppCoder/curso/list"

from django.views.generic.detail import DetailView
class CursoDetalle(DetailView):
    model = Curso
    template = 'AppCoder/curso_detail.html'


