from django.contrib import admin
from .models import Actor

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gender', 'profile_pic', 'movies_field', 'movies_count_field')
    search_fields = ['name']
    list_filter = ['gender']
    fieldsets = (
        ("Maun Subtitle", {'fields': ['name', 'gender', 'profile_pic']}),
        ("Movies", {'fields': ['movies_field']}),
    )
    readonly_fields = ["movies_field"]
    def movies_field(self, obj):
        movie_names = [_obj.name for _obj in obj.movie_set.all()]
        return movie_names
    movies_field.short_description = 'Movies'
    def movies_count_field(self, obj):
        movie_count = obj.movie_set.all().count()
        return movie_count
    movies_count_field.short_description = 'Movies Count'
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False
    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False
    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False
