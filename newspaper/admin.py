from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from newspaper.models import Topic, Newspaper, Redactor
from django.contrib.auth.models import Group


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Newspaper)
class NewspaperAdmin(admin.ModelAdmin):
    list_display = ("title", "published_date")
    list_filter = ("published_date", "topics")
    search_fields = ("title", "content")


@admin.register(Redactor)
class RedactorAdmin(admin.ModelAdmin):
    list_display = ("username", "years_of_experience", "email")
    search_fields = ("username", "email")


admin.site.unregister(Group)