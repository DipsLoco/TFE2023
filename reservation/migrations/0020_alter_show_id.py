# Generated by Django 4.2.1 on 2023-10-21 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0019_alter_locality_postal_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]