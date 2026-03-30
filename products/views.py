from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Product
from .tasks import log_product_view
from django.views.generic import DetailView, CreateView, UpdateView, ListView


class ProductCreateView(CreateView):
    model=Product
    success_url=reverse_lazy('product_create')
    template_name='product/create.html'
    fields = ['name', 'price'] 

class ProductDetailView(DetailView):
    model=Product
    template_name='product/detail.html'
    
    
    def get_object(self, queryset=None):
        # 1. Сначала получаем сам объект товара из базы
        obj = super().get_object(queryset)
        
        # 2. СРАЗУ отправляем задачу в Celery
        log_product_view.delay(obj.name)
        
        # 3. Возвращаем товар, чтобы страница открылась
        return obj 


class ProductListView(ListView):
    model = Product
    template_name = 'product/list.html'
    context_object_name = 'products'


    