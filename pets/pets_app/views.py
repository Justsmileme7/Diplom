from django.shortcuts import render, redirect
from django.views import View
from .models import Pets, Feedback
from .forms import FeedbackForm


class MainPageView(View):
    PAGE_TITLE = 'Pets'

    def get(self, request, *args, **kwargs):
        order = request.GET.get('order', 'back_order')
        sort = request.GET.get('sort', 'date_of_add')
        if order == 'back_order':
            sort = f'-{sort}'

        filter_type = request.GET.get('type', '')
        if filter_type == '':
            pets = Pets.objects.all().order_by(sort)
        else:
            pets = Pets.objects.all().order_by(sort).filter(type=filter_type)

        return render(request, 'mainpage.html',
                      context={"title": self.PAGE_TITLE,
                               'pets_list': pets,
                               })


class PetsPageView(View):

    def get(self, request, id, *args, **kwargs):
        pets = Pets.objects.get(id=id)
        pet_type = pets.type
        return render(request, 'petpage.html',
                      context={"title": pet_type,
                               'pet': pets,
                               })


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
