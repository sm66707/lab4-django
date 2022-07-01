from django.contrib import admin
from .models import Director
from movie.models import Movie

class MovieInLine(admin.StackedInline):
    model = Movie
    extra = 1

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gender', 'profile_pic', 'movies_field')
    search_fields = ['name']
    list_filter = ['gender']
    fieldsets = (
        ("Maun Subtitle", {'fields': ['name', 'gender', 'profile_pic']}),
        ("Movies", {'fields': ['movies_field']}),
    )
    inlines = [MovieInLine]
    readonly_fields = ["movies_field"]
    def movies_field(self, obj):
        movie_names = [_obj.name for _obj in obj.movie_set.all()]
        return movie_names
    movies_field.short_description = 'Movies'
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
    # def get_search_results(self, request, queryset, search_term):
    #     queryset, use_distinct = super(DirectorAdmin, self).get_search_results(request, queryset, search_term)
    #     search_term_list = search_term.split(' ')
    #     if 'movies_field' in search_term_list:
    #        queryset = Movie.objects.annotate(
    #            movie_name = 'movie__name'
    #        ).filter(movie_name__gte=search_term_list['movies_field'])
    #     return queryset, use_distinct
