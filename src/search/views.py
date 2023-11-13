from django.shortcuts import render

from django.views.generic import ListView

from products.models import Products

# Create your views here.
class SearchProductView(ListView):
    queryset = Products.objects.all()
    template_name = "search/view.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        # SearchQuery.objects.create(query=query)
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        print(request.GET)
        query = method_dict.get('q', None)
        print(query)
        if query is not None:
            return Products.objects.search(query)
        return Products.objects.featured()
 