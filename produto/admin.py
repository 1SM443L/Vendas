from django.contrib import admin
from produto.models import*
# Register your models here.

class ProdutoAdmin(admin.ModelAdmin):
    search_field= ["nome"]
    list_display= ('id',"nome", "valor")


admin.site.register(Produto,ProdutoAdmin)
admin.site.register(Categoria)