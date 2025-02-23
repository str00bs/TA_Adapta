from .models import Messages
from rest_framework import permissions, viewsets

from .serializers import MessagesSerializer


class MessagesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer
    permission_classes = [permissions.IsAuthenticated]
