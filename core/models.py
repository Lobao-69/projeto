from django.db import models

class Categorie(models.Model):
    # nome da categoria
    name = models.CharField("Categorias", max_length=15)
    
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Product(models.Model):
    name = models.CharField("Produto", max_length=100)
    description = models.TextField("Descrição", max_length=255)
    price = models.FloatField("Preço do Produto", default=0)
    imagem = models.ImageField("Imagem do Produto", upload_to='images/', blank=True, null=True)
    categorie = models.ForeignKey(Categorie, null=True, blank=True, verbose_name="Categoria", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
                                  
