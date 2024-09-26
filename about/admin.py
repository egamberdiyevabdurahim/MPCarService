from django.contrib import admin

from about.models import (CarouselModel, ServicesAboutModel, AboutModel, TickedModel,
                          ServicesModel, SocialsModel, InfoModel, ExpertTechniciansModel)


@admin.register(CarouselModel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_active', 'created_at')
    list_display_links = list_display
    list_filter = ('is_active', 'is_deleted', 'created_at')
    search_fields = ('title', 'id')
    ordering = ('-created_at',)


@admin.register(ServicesAboutModel)
class ServicesAboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_deleted', 'created_at')
    list_display_links = list_display
    list_filter = ('is_deleted', 'created_at')
    search_fields = ('title', 'id')
    ordering = ('-created_at',)


@admin.register(AboutModel)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_deleted', 'created_at')
    list_display_links = list_display
    list_filter = ('is_deleted', 'created_at')
    search_fields = ('title', 'description', 'experience', 'full_experience',
                     'expert_technicians', 'satisfied_clients', 'complete_projects', 'id')
    ordering = ('-created_at',)


@admin.register(TickedModel)
class TickedAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_deleted', 'created_at')
    list_display_links = list_display
    list_filter = ('is_deleted', 'created_at')
    search_fields = ('name', 'id')
    ordering = ('-created_at',)


@admin.register(ServicesModel)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'main_name', 'title', 'is_deleted', 'created_at')
    list_display_links = list_display
    list_filter = ('is_deleted', 'created_at')
    search_fields = ('main_name', 'title', 'description', 'id')
    ordering = ('-created_at',)


@admin.register(SocialsModel)
class SocialsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'link', 'icon', 'is_deleted', 'created_at')
    list_display_links = list_display
    list_filter = ('is_deleted', 'created_at')
    search_fields = ('name', 'link', 'icon', 'id')
    ordering = ('-created_at',)


@admin.register(InfoModel)
class InfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand_name', 'address', 'phone', 'email', 'created_at')
    list_display_links = list_display
    list_filter = ('is_deleted', 'created_at')
    search_fields = ('brand_name', 'address', 'phone', 'email', 'id')
    ordering = ('-created_at',)


@admin.register(ExpertTechniciansModel)
class ExpertTechniciansAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'is_pinned', 'is_deleted', 'created_at')
    list_display_links = list_display
    list_filter = ('is_deleted', 'created_at', 'is_pinned')
    search_fields = ('first_name', 'last_name', 'description', 'id')
    ordering = ('-created_at',)
