from django.contrib import admin
from .models import Category, Product
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug':('name',)}

'''
Помните, используя prepopulated_fields, мы настраиваем поле slug так, 
чтобы его значение формировалось автоматически из поля name. 
Атрибут list_editable в классе ProductAdmin добавляет возможность изменять 
перечисленные поля со страницы списка товаров, не переходя к форме 
редактирования товара. Отметим, что все поля, перечисленные в list_editable, 
должны быть добавлены в атрибут list_display, 
иначе они не будут видны на странице списка объектов. 
'''