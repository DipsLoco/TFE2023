# Generated by Django 4.2.1 on 2023-05-16 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_alter_show_bookable_alter_show_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]