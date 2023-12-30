from django.contrib import admin
from .models import Todo, Tag

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed', '_tags')

    def _tags(self, row):
        return ', '.join([x.name for x in row.tag.all()])


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
    def _str_(self):
        return self.name

admin.site.register(Todo, TodoAdmin)
admin.site.register(Tag, TagAdmin)