# Generated by Django 2.1.3 on 2018-11-23 02:14

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20181123_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('コラム', 'コラム'), ('カスタム婚', 'カスタム婚'), ('item_key3', 'Item title 1.3'), ('item_key4', 'Item title 1.4'), ('item_key5', 'Item title 1.5')], max_length=39),
        ),
    ]
