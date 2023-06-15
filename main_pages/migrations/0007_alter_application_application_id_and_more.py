# Generated by Django 4.2.1 on 2023-06-12 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_pages', '0006_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='application_id',
            field=models.CharField(max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='client',
            name='clients_id',
            field=models.CharField(max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='color',
            name='color_id',
            field=models.CharField(max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='delivery_id',
            field=models.CharField(max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='deliveryservice',
            name='delivery_service_id',
            field=models.CharField(max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_id',
            field=models.CharField(max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='incomingproduct',
            name='delivery_number',
            field=models.CharField(max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='jobtitle',
            name='job_title_id',
            field=models.CharField(max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='material',
            name='material_id',
            field=models.CharField(max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.CharField(max_length=36, primary_key=True, serialize=False),
        ),
    ]
