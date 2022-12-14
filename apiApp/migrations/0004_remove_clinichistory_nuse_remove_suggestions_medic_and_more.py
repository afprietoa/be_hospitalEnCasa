# Generated by Django 4.1.1 on 2022-10-13 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apiApp', '0003_remove_vitalsigns_historic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clinichistory',
            name='nuse',
        ),
        migrations.RemoveField(
            model_name='suggestions',
            name='medic',
        ),
        migrations.RemoveField(
            model_name='vitalsigns',
            name='patient',
        ),
        migrations.AddField(
            model_name='vitalsigns',
            name='historic',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='vital_signs', to='apiApp.clinichistory'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='suggestions',
            name='historic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suggestions', to='apiApp.clinichistory'),
        ),
    ]
