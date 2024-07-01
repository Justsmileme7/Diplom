from django.shortcuts import render
from django.views import View
from .models import Pets, Feedback


# Create your views here.
class MainPageView(View):
    PAGE_TITLE = 'Pets'

    def get(self, request, *args, **kwargs):
        """sort_by = request.GET.get('sort', 'date_of_create')  # получаем из нтмл переменную sort
        order_by = request.GET.get('order', 'back_order')
        sort_by = sort_by if order_by == 'wright_order' else f'-{sort_by}' """
        pets = Pets.objects.all()  # достаем объекты из базы данных из таблицы pets

        return render(request, 'mainpage.html',
                      context={"title": self.PAGE_TITLE,
                               'pets_list': pets,
                               })


class PetsPageView(View):

    def get(self, request, id, *args, **kwargs):
        news = News.objects.get(id=id)  # достаем одну новость по ИД из базы данных из таблицы news
        title = news.title
        return render(request, 'newspage.html',
                      context={"title": title,
                               'news': news,
                               })
# Create your views here.
