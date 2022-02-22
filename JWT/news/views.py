from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Articles
from django.core.paginator import Paginator


def news(request):
    base_news = Articles.objects.order_by('date').reverse()
    p = Paginator(base_news, 5)
    count_list = p.page_range
    page_number = request.GET.get('page')
    page = p.get_page(page_number)
    return render(request, 'news/news.html', {'page': page, 'count_list': count_list})


class NewsDetailViews(DetailView):
    model = Articles
    template_name = 'news/details_news.html'
    context_object_name = 'article'
