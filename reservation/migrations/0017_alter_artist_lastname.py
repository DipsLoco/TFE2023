# Generated by Django 4.2.1 on 2023-05-21 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0016_alter_representationuser_representation_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='lastname',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
