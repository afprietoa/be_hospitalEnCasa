# Generated by Django 4.1.1 on 2022-09-29 23:59

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('rol', models.CharField(max_length=50, verbose_name='Rol')),
                ('doc_type', models.CharField(default='', max_length=50, verbose_name='Doc-Type')),
                ('doc_number', models.BigIntegerField(default=0, unique=True)),
                ('first_name', models.CharField(default='', max_length=50, verbose_name='First_Name')),
                ('last_name', models.CharField(default='', max_length=50, verbose_name='Last_Name')),
                ('e_mail', models.EmailField(max_length=100, verbose_name='Email')),
                ('cellphone', models.BigIntegerField(default=0)),
                ('genre', models.CharField(default='', max_length=50, verbose_name='Genre')),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='Username')),
                ('password', models.CharField(max_length=256, verbose_name='Password')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ClinicHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_time', models.DateTimeField(default=datetime.datetime.now, max_length=50, verbose_name='Date-Time')),
                ('diagnostic', models.CharField(default='', max_length=50, verbose_name='Diagnostic')),
                ('description', models.CharField(default='', max_length=50, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('relationship', models.CharField(default='', max_length=80, verbose_name='Relationship')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Medic',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('professional_card', models.BigIntegerField(default=0, unique=True)),
                ('speciality', models.CharField(default='', max_length=50, verbose_name='Speciality')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('birth_date', models.DateField(default=datetime.date.today, max_length=50, verbose_name='Birth_Date')),
                ('address', models.CharField(default='', max_length=50, verbose_name='Address')),
                ('city', models.CharField(default='', max_length=50, verbose_name='City')),
                ('longitude', models.CharField(default='', max_length=50, verbose_name='Longitude')),
                ('latitude', models.CharField(default='', max_length=50, verbose_name='Latitude')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VitalSigns',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_time', models.DateTimeField(default=datetime.datetime.now, max_length=50, verbose_name='Date_Time')),
                ('oximetry', models.CharField(default='', max_length=50, verbose_name='Oximetry')),
                ('glycemia', models.CharField(default='', max_length=50, verbose_name='Glycemia')),
                ('blood_pressure', models.CharField(max_length=50, verbose_name='Blood_Pressure, default=')),
                ('temperature', models.CharField(default='', max_length=50, verbose_name='Temperature')),
                ('heart_rate', models.CharField(default='', max_length=50, verbose_name='Heart_Rate')),
                ('respiratory_rate', models.CharField(default='', max_length=50, verbose_name='Respiratory_Rate')),
                ('historic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiApp.clinichistory')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiApp.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Suggestions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(default='', max_length=50, verbose_name='Description')),
                ('historic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiApp.clinichistory')),
                ('medic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiApp.medic')),
            ],
        ),
        migrations.CreateModel(
            name='PatientFamiliar',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('familiar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiApp.familiar')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiApp.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('professional_card', models.BigIntegerField(default=0, unique=True)),
                ('speciality', models.CharField(default='', max_length=50, verbose_name='Speciality')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='clinichistory',
            name='medic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiApp.medic'),
        ),
        migrations.AddField(
            model_name='clinichistory',
            name='nuse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiApp.nurse'),
        ),
        migrations.AddField(
            model_name='clinichistory',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiApp.patient'),
        ),
        migrations.CreateModel(
            name='Auxiliar',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('professional_card', models.BigIntegerField(default=0, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]