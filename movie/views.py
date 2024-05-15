from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import MovieSerializer
from .models import Movie
from typing import Any

class MoviesList(ListCreateAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self)-> Any:
        return self.queryset.all()

class MovieDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    lookup_field = "name"

    def get_queryset(self) -> Any:
        return self.queryset.all()
