from django.shortcuts import render
from rest_framework import viewsets

from .serializers import NaturalPersonSerializer, LegalEntitySerializer, EquityClassSerializer, EquityTokenSerializer, EmploymentRelationSerializer, OfficerRelationSerializer, DirectorRelationSerializer

from .models import NaturalPerson, LegalEntity, EquityClass, EquityToken, EmploymentRelation, OfficerRelation, DirectorRelation

# Create your views here.

class NaturalPersonViewSet(viewsets.ModelViewSet):
    queryset = NaturalPerson.objects.all().order_by('full_name')
    serializer_class = NaturalPersonSerializer

class LegalEntityViewSet(viewsets.ModelViewSet):
    queryset = LegalEntity.objects.all().order_by('last_updated')
    serializer_class = LegalEntitySerializer

class EquityClassViewSet(viewsets.ModelViewSet):
    queryset = EquityClass.objects.all().order_by('issuing_entity')
    serializer_class = EquityClassSerializer

class EquityTokenViewSet(viewsets.ModelViewSet):
    queryset = EquityToken.objects.all().order_by('issuing_entity')
    serializer_class = EquityTokenSerializer

class EmploymentRelationViewSet(viewsets.ModelViewSet):
    queryset = EmploymentRelation.objects.all().order_by('employer')
    serializer_class = EmploymentRelationSerializer

class OfficerRelationViewSet(viewsets.ModelViewSet):
    queryset = OfficerRelation.objects.all().order_by('company')
    serializer_class = OfficerRelationSerializer

class DirectorRelationViewSet(viewsets.ModelViewSet):
    queryset = DirectorRelation.objects.all().order_by('company')
    serializer_class = DirectorRelationSerializer
