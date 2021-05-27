from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from .models import Contact
from .serializers import ContactSerializer
from .permissions import IsOwnerOrReadOnly


class ContactViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows contacts to be created, read, updated and deleted.
    """
    queryset = Contact.objects.all().order_by('name')
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        """
        List the authenticated user contacts 
        """
        user = self.request.user
        return Contact.objects.filter(owner=user, deleted=False)

    def perform_create(self, serializer):
        """
        Save contact owner on create
        """
        serializer.save(owner=self.request.user)

    def destroy(self, request, *args, **kwargs):
        contact = self.get_object()
        contact.deleted = True
        contact.save()
        return Response(status=HTTP_204_NO_CONTENT)
