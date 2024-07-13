from django.contrib import admin

from .models import Model, Mark, Part


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_visible',
        'mark_name'
    )
    list_editable = (
        'is_visible',
    )
    list_filter = ('mark_id',)


@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_visible',
    )
    list_editable = (
        'is_visible',
    )


@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_visible',
    )
    list_editable = (
        'is_visible',
    )
