from django.contrib import admin
from pets_app.models import Pets, Feedback, Photo
from django.utils.safestring import mark_safe


class PhotoInline(admin.StackedInline):
    model = Photo


@admin.register(Pets)
class PetsAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'breed', 'image', 'description', 'age', 'place', 'date_of_add')
    search_fields = ('name', 'type', 'breed', 'place')
    ordering = ('name', 'type', 'breed', 'place')
    inlines = (PhotoInline,)

    def preview(self, instance: Pets):
        if instance.image:
            return mark_safe(f'<img style="max-width: 100px" src="{instance.image.url}" alt="">')
        return mark_safe('Without picture')


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'context_of_comment', 'phone')


@admin.register(Photo)
class Photo(admin.ModelAdmin):
    list_display = ('pet', 'photo')

    def preview(self, instance: Photo):
        if instance.image:
            return mark_safe(f'<img style="max-width: 100px" src="{instance.image.url}" alt="">')
        return mark_safe('Without picture')
