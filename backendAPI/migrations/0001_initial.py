# Generated by Django 3.2.5 on 2021-07-13 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EquityClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equity_class_type', models.CharField(max_length=100)),
                ('number_authorized', models.IntegerField()),
                ('last_updated', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='LegalEntity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entity_name', models.CharField(max_length=100)),
                ('entity_type', models.CharField(max_length=100)),
                ('state_of_formation', models.CharField(max_length=2)),
                ('last_updated', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='NaturalPerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('residency_state', models.CharField(max_length=2)),
                ('last_updated', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='OfficerRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('office', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('term', models.IntegerField()),
                ('incentive_equity_award', models.CharField(max_length=500, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendAPI.legalentity')),
                ('officer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendAPI.naturalperson')),
            ],
        ),
        migrations.CreateModel(
            name='EquityToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_issued', models.IntegerField()),
                ('date_of_issuance', models.DateField()),
                ('equity_class_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendAPI.equityclass')),
                ('issuing_entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issuing_entity', to='backendAPI.legalentity')),
                ('legal_entity_holder', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='legal_entity_holder', to='backendAPI.legalentity')),
                ('natural_person_holder', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backendAPI.naturalperson')),
            ],
        ),
        migrations.AddField(
            model_name='equityclass',
            name='issuing_entity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendAPI.legalentity'),
        ),
        migrations.CreateModel(
            name='EmploymentRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=100, null=True)),
                ('start_date', models.DateField()),
                ('term', models.IntegerField()),
                ('pay', models.IntegerField()),
                ('at_will', models.BooleanField()),
                ('at_will_exceptions', models.CharField(max_length=500, null=True)),
                ('incentive_equity_award', models.CharField(max_length=500, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendAPI.naturalperson')),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendAPI.legalentity')),
            ],
        ),
        migrations.CreateModel(
            name='DirectorRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=100, null=True)),
                ('committees', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('term', models.IntegerField()),
                ('incentive_equity_award', models.CharField(max_length=500, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendAPI.legalentity')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendAPI.naturalperson')),
            ],
        ),
    ]
