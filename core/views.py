from django.http.response import HttpResponse as HttpResponse
from django.views.generic import TemplateView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth import authenticate, login as auth_login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import *



class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Adiciona ao contexto todas as categorias existentes no banco de dados.
        context['categorias'] = Categorie.objects.all()
        busca = self.request.GET.get('busca')
        filtro_categoria = self.request.GET.get('filter')

        # Obtém todos os objetos Product do banco de dados e os ordena pelo campo 'id' de forma decrescente.
        queryset = Product.objects.all().order_by('-id')
        if busca:
            queryset = queryset.filter(name__icontains=busca)

        # Se houver uma categoria especificada, filtra os produtos por essa categoria.
        if filtro_categoria:
            queryset = queryset.filter(categorie__name=filtro_categoria)
        context['produtos'] = queryset
        return context

# Define a classe ProductView, que herda de DetailView, indicando que é uma view para exibir detalhes de um objeto do banco de dados.
class ProductView(DetailView):
    model = Product
    template_name = 'product.html'

    # Define o nome da variável de contexto que conterá o objeto Product a ser passado para o template.
    context_object_name = 'produto'
    

# Define a classe ProductsEditView, que herda de TemplateView, indicando que é uma view baseada em template.
class ProductsEditView(TemplateView):
    template_name = 'products-edit.html'

    # Sobrescreve o método get_context_data da classe base TemplateView para adicionar dados ao contexto da view.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Obtém o parâmetro 'busca' da requisição GET, que pode conter um termo de busca.
        busca = self.request.GET.get('busca')
        if busca:
            # Se houver um termo de busca, adiciona ao contexto os produtos filtrados pelo nome que contenha o termo de busca.
            context['produtos'] = Product.objects.filter(name__icontains=busca).order_by('-id')
        else:
            # Se não houver um termo de busca, adiciona ao contexto todos os produtos existentes no banco de dados, ordenados pelo campo 'id' de forma decrescente.
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
    
    
class LoginView(View):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        # Se o usuário já estiver logado, redireciona para a página inicial
        if request.user.is_authenticated:
            return redirect('index')

        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        # Processa o formulário de login
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:  # Se o usuário existir, faz o login
            auth_login(request, user)
            return redirect('index')
        else:
            return HttpResponse('Credenciais inválidas. Tente novamente.')
        
def Desconectar(request):
    logout(request)
    return redirect('index')