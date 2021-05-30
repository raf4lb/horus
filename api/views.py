from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, renderer_classes
from .models import Contact
from .serializers import ContactSerializer
from .permissions import IsOwnerOrReadOnly


class ContactViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows contacts to be created, read, updated and deleted.
    """
    queryset = Contact.objects.order_by('name')
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    class Meta:
        ordering = ['name']

    def get_queryset(self):
        """
        List the authenticated user contacts
        """
        user = self.request.user
        return Contact.objects.filter(owner=user, deleted=False)

    def create(self, request, *args, **kwargs):
        """
        Create a contact
        """
        telephone = request.data.get('telephone')
        if telephone:
            if Contact.objects.filter(owner=request.user, telephone=telephone, deleted=False).exists():
                return Response(status=HTTP_400_BAD_REQUEST)
        return super().create(self, request, *args, **kwargs)

    def perform_create(self, serializer):
        """
        Save the contact owner before create
        """
        serializer.save(owner=self.request.user)

    def update(self, request, *args, **kwargs):
        """
        Create a contact if the phone does not exist or if it exists, but is deleted
        """
        telephone = request.data.get('telephone')
        if telephone and telephone != self.get_object().telephone:
            if Contact.objects.filter(owner=request.user, telephone=telephone, deleted=False).exists():
                return Response(status=HTTP_400_BAD_REQUEST)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        contact = self.get_object()
        contact.deleted = True
        contact.save()
        return Response(status=HTTP_204_NO_CONTENT)


@api_view(('GET',))
@renderer_classes((JSONRenderer,))
def user_info(request):
    if request.user.is_authenticated and request.method == 'GET':
        return Response({
            'id': request.user.pk,
            'name': request.user.get_full_name(),
            'email': request.user.email,
        })
    else:
        return Response(status=HTTP_400_BAD_REQUEST)
