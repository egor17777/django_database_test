from django.contrib import admin
from django.template import Origin
from .models import Book
from django.db.models import QuerySet
# Register your models here.

class Rating_filter(admin.SimpleListFilter):
    title = "Filter for rating"
    parameter_name = "rating"

    def lookups(self, request, model_admin):
        return [
            ("<40", "Low"),
            ("40 to 60", "medium"),
            ("60 to 80",  "high"),
            ("80>", "very high")
        ]
    
    def queryset(self, request, queryset: QuerySet):
        if self.value()=="<40":
            return queryset.filter(rating__lt=40)
        if self.value()=="40 to 60":
            return queryset.filter(rating__gte=40).filter(rating__lt = 60)
        if self.value()=="60 to 80":
            return queryset.filter(rating__gte=60).filter(rating__lt = 80)
        if self.value()=="80>":
            return queryset.filter(rating__gte=80)
        

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    #exclude = ['slug']
    prepopulated_fields = {"slug" : ('title', )}
    list_display = ['title', 'rating', 'origin', 'author', 'rating_status']
    list_editable = ['rating', 'origin', 'author']
    ordering = ['-rating', 'title']
    actions = ['set_europe', 'set_usa']
    search_fields = ['title', 'author']
    list_filter = ['title', 'author', Rating_filter]

    @admin.display(ordering= '-rating', description= 'Stats')
    def rating_status(self, mov:Book):
        if mov.rating < 50:
            return "You shouldn't read it"
        if mov.rating < 70:
            return "The book is not very"
        if mov.rating < 85:
            return "Worth reading"
        else:
            return "Recommended reading"
    @admin.action(description="SET EUROPE")
    def set_europe(self, request, queryset:QuerySet):
        queryset.update(origin = 'EUR')

    @admin.action(description="SET USA")
    def set_usa(self, request, queryset:QuerySet):
        count = queryset.update(origin = 'EUR')
        self.message_user(request, f"You edited {count} entry.")