# Generated by Django 4.2.1 on 2023-06-18 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_pages', '0010_alter_collection_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default=10, verbose_name='Остаток на складе'),
        ),
    ]