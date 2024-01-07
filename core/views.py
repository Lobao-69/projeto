from django.http.response import HttpResponse as HttpResponse
from django.views.generic import TemplateView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import *


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categorie.objects.all()
        busca = self.request.GET.get('busca')

        filtro_categoria = self.request.GET.get('filter')

        queryset = Product.objects.all().order_by('-id')

        if busca:
            queryset = queryset.filter(name__icontains=busca)

        if filtro_categoria:
            queryset = queryset.filter(categorie__name=filtro_categoria)

        context['produtos'] = queryset

        return context
    

class ProductView(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'produto'
    

class ProductsEditView(TemplateView):
    template_name = 'products-edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        busca = self.request.GET.get('busca')
        
        if busca:
            context['produtos'] = Product.objects.filter(name__icontains=busca).order_by('-id')
        else:
            context['produtos'] = Product.objects.all().order_by('-id')
        
        return context

class ProductEditView(UpdateView):
    model = Product
    template_name = 'product-form.html'
    fields = ['name', 'description', 'price', 'categorie']

    def get_success_url(self):
        return reverse_lazy('product', kwargs={'pk': self.object.pk})


class CreateProductView(CreateView):
    model = Product
    template_name = 'create-product.html'
    fields = ['name', 'description', 'imagem', 'price', 'categorie']
    
    def get_success_url(self):
        
        return reverse_lazy('product', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product-delete.html'
    success_url = reverse_lazy('products-edit')