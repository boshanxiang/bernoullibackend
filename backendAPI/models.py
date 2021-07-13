from django.db import models

class NaturalPerson(models.Model):
    full_name = models.CharField(max_length = 100)
    residency_state = models.CharField(max_length=2)
    last_updated = models.DateField()
    previous_records = {}

    # def __str__(self):
    #     return self.full_name

class LegalEntity(models.Model):
    entity_name = models.CharField(max_length = 100)
    entity_type = models.CharField(max_length = 100)
    state_of_formation = models.CharField(max_length=2)
    last_updated = models.DateField()
    previous_records = {}

class EquityClass(models.Model):
    issuing_entity = models.ForeignKey(LegalEntity, on_delete=models.CASCADE)
    equity_class_type = models.CharField(max_length = 100)
    number_authorized = models.IntegerField()
    last_updated = models.DateField()
    previous_records = {}

class EquityToken(models.Model):
    issuing_entity = models.ForeignKey(LegalEntity, on_delete=models.CASCADE, related_name="issuing_entity")
    equity_class_type = models.ForeignKey(EquityClass, on_delete=models.CASCADE)
    natural_person_holder = models.ForeignKey(NaturalPerson, on_delete=models.CASCADE, null=True)
    legal_entity_holder = models.ForeignKey(LegalEntity, on_delete=models.CASCADE, null=True, related_name="legal_entity_holder")
    number_issued = models.IntegerField()
    date_of_issuance = models.DateField()
    previous_records = {}

class EmploymentRelation(models.Model):
    employer = models.ForeignKey(LegalEntity, on_delete=models.CASCADE)
    employee = models.ForeignKey(NaturalPerson, on_delete=models.CASCADE)
    position = models.CharField(max_length = 100, null=True)
    start_date = models.DateField()
    term = models.IntegerField()
    pay = models.IntegerField()
    at_will = models.BooleanField()
    at_will_exceptions = models.CharField(max_length = 500, null=True)
    incentive_equity_award = models.CharField(max_length = 500, null=True)
    previous_records = {}

class OfficerRelation(models.Model):
    company = models.ForeignKey(LegalEntity, on_delete=models.CASCADE)
    officer = models.ForeignKey(NaturalPerson, on_delete=models.CASCADE)
    office = models.CharField(max_length = 100)
    start_date = models.DateField()
    term = models.IntegerField()
    incentive_equity_award = models.CharField(max_length = 500, null=True)
    previous_records = {}

class DirectorRelation(models.Model):
    company = models.ForeignKey(LegalEntity, on_delete=models.CASCADE)
    director = models.ForeignKey(NaturalPerson, on_delete=models.CASCADE)
    position = models.CharField(max_length = 100, null=True)
    committees = models.CharField(max_length = 200)
    start_date = models.DateField()
    term = models.IntegerField()
    incentive_equity_award = models.CharField(max_length = 500, null=True)
    previous_records = {}

# Create your models here.
