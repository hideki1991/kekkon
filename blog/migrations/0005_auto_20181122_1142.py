# Generated by Django 2.1.3 on 2018-11-22 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20181122_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='document',
            field=models.FileField(upload_to=''),
        ),
    ]
