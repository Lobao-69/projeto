"""
URL configuration for e_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import IndexView, ProductsEditView, ProductView, ProductEditView, CreateProductView, ProductDeleteView, LoginView, Desconectar
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('product/<int:pk>', ProductView.as_view(), name='product'),
    path('product/create/', CreateProductView.as_view(), name='create-product'),
    path('products-edit/', ProductsEditView.as_view(), name='products-edit'),
    path('product/<int:pk>/edit', ProductEditView.as_view(), name='product-edit'),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name='product-delete'),
    path('login/', LoginView.as_view(), name='login'),
    path('desconectar/', Desconectar, name='desconectar')
]

# Verifica se o projeto está em modo de desenvolvimento (DEBUG) e, se estiver, adiciona a rota para servir arquivos de mídia.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
