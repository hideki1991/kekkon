# Generated by Django 2.1.3 on 2018-11-21 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='year_in_school',
            new_name='category',
        ),
    ]
