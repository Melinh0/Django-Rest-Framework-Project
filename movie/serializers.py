from .models import Movie
from rest_framework import serializers

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

    def validate(self, attrs):
        existing_movie = Movie.objects.filter(
            name=attrs["name"], director=attrs["director"], duration=attrs["duration"]
        )

        if existing_movie.exists():
            raise serializers.ValidationError({"error": "movie_already_exists"})

        return attrs

