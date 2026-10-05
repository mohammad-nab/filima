import django_filters as filters
from .models import Content


class ContentFilter(filters.FilterSet):
    genre = filters.CharFilter(field_name='content_genres__genre__slug')
    release_year_min = filters.NumberFilter(field_name='release_year', lookup_expr='gte')
    release_year_max = filters.NumberFilter(field_name='release_year', lookup_expr='lte')
    imdb_rate_min = filters.NumberFilter(field_name='imdb_rate', lookup_expr='gte')

    class Meta:
        model = Content
        fields = [
            "type",
            "is_free",
            "is_dubbed",
            "age_rate",
        ]