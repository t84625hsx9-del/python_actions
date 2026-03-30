from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Product
from .tasks import log_product_view
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView


class ProductCreateView(CreateView):
    model=Product
    success_url=reverse_lazy('product_create')
    template_name='product/create.html'

class ProductDetailView(DetailView):
    model=Product
    template_name='product/detail.html'

    def get_object(self):
        obj = super().get_object()
        # Вызываем задачу логирования просмотра
        log_product_view.delay(obj.name) 
        return obj
    