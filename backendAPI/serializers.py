#serializers.py

from rest_framework import serializers

from .models import NaturalPerson, LegalEntity, EquityClass, EquityToken, EmploymentRelation, OfficerRelation, DirectorRelation

class NaturalPersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NaturalPerson
        fields = ('id', 'full_name', 'residency_state', 'last_updated', 'previous_records')

class LegalEntitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LegalEntity
        fields = ('id', 'entity_name', 'entity_type', 'state_of_formation', 'last_updated', 'previous_records')

class EquityClassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EquityClass
        fields = ('id', 'issuing_entity', 'equity_class_type', 'number_authorized', 'last_updated', 'previous_records')

class EquityTokenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EquityToken
        fields = ('id', 'issuing_entity', 'equity_class_type', 'natural_person_holder', 'legal_entity_holder', 'number_issued', 'date_of_issuance', 'previous_records')

class EmploymentRelationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EmploymentRelation
        fields = ('id', 'employer', 'employee', 'position', 'start_date', 'term', 'pay', 'at_will', 'at_will_exceptions', 'incentive_equity_award', 'previous_records')

class OfficerRelationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OfficerRelation
        fields = ('id', 'company', 'officer', 'office', 'start_date', 'term', 'incentive_equity_award', 'previous_records')

class DirectorRelationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DirectorRelation
        fields = ('id', 'company', 'director', 'position', 'committees', 'start_date', 'term', 'incentive_equity_award', 'previous_records')
