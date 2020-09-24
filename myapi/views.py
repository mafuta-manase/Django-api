from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ContactsSerializer
from .models import Contacts

class ContactsViewSet(viewsets.ModelViewSet):
    queryset = Contacts.objects.all().order_by('name')
    serializer_class = ContactsSerializer
