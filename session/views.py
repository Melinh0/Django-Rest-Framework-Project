from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Session
from .serializers import SessionSerializer, SessionDetailSerializer
from typing import Any

class SessionListCreateView(ListCreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer 

    def get_serializer_class(self) -> Any:
        return SessionDetailSerializer

class SessionDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Session.objects.all()

    def get_serializer_class(self) -> Any:
        return SessionDetailSerializer if self.request.method == "GET" else SessionSerializer