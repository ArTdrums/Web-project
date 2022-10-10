# Generated by Django 4.1 on 2022-10-07 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0006_reviews'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reviews',
            options={'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.AlterField(
            model_name='reviews',
            name='text_reviews',
            field=models.TextField(max_length=2000, verbose_name='Текст отзыва'),
        ),
    ]