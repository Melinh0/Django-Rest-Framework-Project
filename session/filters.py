from rest_framework import filters

class SessionFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        movie_id = request.query_params.get('name')
        theater_id = request.query_params.get('number')
        if movie_id:
            queryset = queryset.filter(movie_id=movie_id)
        if theater_id:
            queryset = queryset.filter(theater_id=theater_id)
        return queryset
