from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Products , Comment



# Create your views here.
def Index(request):
    return render(request , "Index/Index.html")
class ProductView(ListView):
    template_name = 'Index/product.html'
    context_object_name = 'data'
    model = Products
class DetailProductView(DetailView):
    template_name = "Index/detai.html"
    model = Products
    context_object_name = 'data'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(product=self.object)

        return context
