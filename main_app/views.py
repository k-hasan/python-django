from django.views.generic import TemplateView, ListView


from . models import QuoteCategory
from . models import Quote

from . models import PostCategory
from . models import Post


class IndexView(TemplateView):
    template_name = "index.html"


class HomeView(ListView):
    template_name = "home.html"
    model = Quote

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.select_related('quote_category')


class AboutView(ListView):
    template_name = "about.html"
    model = Post

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.select_related('post_category')

