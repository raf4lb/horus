from .models import Contact
from rest_framework import serializers


class ContactSerializer(serializers.ModelSerializer):
    '''
    Serializer for contact model
    '''

    class Meta:
        model = Contact
        fields = ['id', 'owner', 'name', 'telephone']
