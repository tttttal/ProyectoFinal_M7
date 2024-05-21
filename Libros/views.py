from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro
from .forms import LibroForm

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'lista_libros.html', {'libros': libros})

def libros_por_genero(request, genero):
    libros = Libro.objects.filter(genero=genero)
    return render(request, 'libros_por_genero.html', {'libros': libros, 'genero': genero})

def libros_por_autor(request, autor_id):
    libros = Libro.objects.filter(autor_id=autor_id)
    return render(request, 'libros_por_autor.html', {'libros': libros})

def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm()
    return render(request, 'crear_libro.html', {'form': form})

def ver_libro(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    return render(request, 'ver_libro.html', {'libro': libro})

def actualizar_libro(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'actualizar_libro.html', {'form': form})

def borrar_libro(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    if request.method == 'POST':
        libro.delete()
        return redirect('lista_libros')
    return render(request, 'borrar_libro.html', {'libro': libro})