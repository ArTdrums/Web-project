# Generated by Django 4.1 on 2022-09-25 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='data_puble',
            new_name='data_publ',
        ),
    ]
