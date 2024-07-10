from django.shortcuts import render, redirect
from django.views import View
from .models import Pets, Feedback
from .forms import FeedbackForm


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
        pets = Pets.objects.get(id=id)  # достаем одну новость по ИД из базы данных из таблицы news
        pet_type = pets.type
        return render(request, 'petpage.html',
                      context={"title": pet_type,
                               'pet': pets,
                               })


# Create your views here.
class FeedbackPageView(View):

    def get(self, request, *args, **kwargs):
        form = FeedbackForm()
        return render(request, 'feedback.html', {'form': form})

    def post(self, request, *args, **kwargs):

        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)

            feedback.save()
            form.save_m2m()
            return redirect('mainpage')


        return render(request, 'feedback.html', {'form': form})
