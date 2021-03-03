
from django.contrib import admin
from django.urls import path ,include



# Deploys
# from django.conf import settings
# from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    path('',include('proveedorApp.urls')),
    path('',include('gruposApp.urls')),
    path('',include('boletaApp.urls')),
    path('',include('zapatillasApp.urls')),
    path('',include('ventaApp.urls')),
    
    path('',include('kardexApp.urls')),
    path('',include('verZapatillasApp.urls')),
    
    path('',include('GenerarPDFApp.urls')),

    path('',include('users.urls')),
] 


# Deploy intento 2

# urlpatterns = [
#     path('admin/', admin.site.urls),

#     path('',include('proveedorApp.urls')),
#     path('',include('gruposApp.urls')),
#     path('',include('boletaApp.urls')),
#     path('',include('zapatillasApp.urls')),
#     path('',include('ventaApp.urls')),
    
#     path('',include('kardexApp.urls')),
#     path('',include('verZapatillasApp.urls')),
    
#     path('',include('GenerarPDFApp.urls')),

#     path('',include('users.urls')),
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# Deploy intento 1 funca
# urlpatterns = [
#     path('admin/', admin.site.urls),

#     path('',include('proveedorApp.urls')),
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
