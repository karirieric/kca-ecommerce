from typing import Any, Dict
from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from carts.models import Cart

from .models import Products


class ProductFeaturedListView(ListView):
    template_name = "products/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Products.objects.all().featured()
    
class ProductFeaturedDetailView(DetailView):
    template_name = "products/featured-detail.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Products.objects.all().featured()



class ProductListView(ListView):
    queryset = Products.objects.all()
    template_name = "products/list.html"

    # def get_context_data(self, *args, **kwargs):
    #    context =super(ProductListView, self).get_context_data(*args, **kwargs)
    #    print(context)
    #    return context


def product_list_view(request):
    queryset = Products.objects.all()
    context = {
        'object_list': queryset
    }
    return render (request, "products/list.html", context)

class ProductDetailSlugView(DetailView):
    queryset = Products.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context ['cart'] = cart_obj
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        # instance = Products.objects.get_by_id(pk)
        try:
            instance = Products.objects.get(slug=slug, active=True)
        except Products.DoesNotExist:
            raise Http404("Product Doesn't Exist 🥲")
        except Products.MultipleObjectsReturned:
            qs = Products.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("404 Error 🥲")
        return instance
    
        
class ProductDetailView(DetailView):
    queryset = Products.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
       context =super(ProductDetailView, self).get_context_data(*args, **kwargs)
       print(context)
       return context
    
    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Products.objects.get_by_id(pk)
        if instance is None:
            raise Http404("404 Error 🥲")
        return instance

 
def product_detail_view(request, pk, *args, **kwargs):
    instance = Products.objects.get(pk=pk, featured=True)
    # instance = get_object_or_404(Products, pk=pk)

    # try:
    #     instance = Products.objects.get(id=pk)
    # except Products.DoesNotExist:
    #     print('No product here')
    #     raise Http404("404 Error 🥲")
    # except:
    #     print('Huh?')

    instance = Products.objects.get_by_id(pk)
    if instance is None:
        raise Http404("404 Error 🥲")

    # print(instance)

    # qs = Products.objects.filter(id=pk)

    # # print(qs)
    # if qs.exists() and qs.count()==1:
    #     instance = qs.first()
    # else:
    #     raise Http404("404 Error 🥲")
    context = {
        'object': instance
    }
    return render(request, "products/detail.html", context)