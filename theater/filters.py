from rest_framework import filters

class TheaterFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        name = request.query_params.get('number')
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


