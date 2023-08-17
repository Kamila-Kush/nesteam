from django.contrib import admin
from .models import *

admin.site.register(Studio)
admin.site.register(Game)

class GameInline(admin.StackedInline):
    model = Game
    extra = 1

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    inlines = [GameInline]
