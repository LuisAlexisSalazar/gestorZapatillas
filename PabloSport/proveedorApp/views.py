from django.shortcuts import render, HttpResponse


from proveedorApp.models import Proveedor
from gruposApp.models import Grupo


from django.db.models import Count
# Create your views here.


def base(request):
    return render(request, "proveedorApp/base.html")




# CRUD proveedores
def get_all_proveedores():
    listaProveedores=Proveedor.objects.all()
    return listaProveedores


def IngresarProveedor(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]

        proveedor_nuevo = Proveedor(nombre=nombre)
        proveedor_nuevo.save()

        listaProveedores=Proveedor.objects.annotate(amount_grupos=Count('grupo'))

        return render(request, "proveedorApp/ingresarProveedor.html",{"proveedores":listaProveedores})
    
    else:
        
        # Recordar que annotate por cada fila añade una columna de lo que quieras añadir
        # listaProveedores=Proveedor.objects.annotate(amount_grupos=Count('grupo'))
        listaProveedores=Proveedor.objects.annotate(amount_grupos=Count('grupo'))


        #Equivalencia: SELECT creador_id ,count(creador_id) from gruposApp_grupo GROUP By creador_id;
        return render(request, "proveedorApp/ingresarProveedor.html",{"proveedores":listaProveedores})


def eliminarProveedor(request,idProveedor):
    proveedor=Proveedor.objects.get(id=idProveedor)
    proveedor.delete()

    listaProveedores=Proveedor.objects.annotate(amount_grupos=Count('grupo'))
    return render(request, "proveedorApp/ingresarProveedor.html",{"proveedores":listaProveedores})


def editarProveedor(request,idProveedor):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        
        
        proveedor=Proveedor.objects.get(id=idProveedor)
        proveedor.nombre=nombre
        proveedor.save()

        grupos=Grupo.objects.filter(creador=proveedor).order_by("-fechaIngreso")
        

        return render(request, "proveedorApp/editarProveedor.html",{"proveedor":proveedor,'grupos':grupos})
    
    else:

        proveedor=Proveedor.objects.get(id=idProveedor)

        grupos=Grupo.objects.filter(creador=proveedor).order_by("-fechaIngreso")

        return render(request, "proveedorApp/editarProveedor.html",{"proveedor":proveedor,'grupos':grupos})


