# Generated by Django 4.1.5 on 2023-01-17 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='product',
            name='review',
            field=models.TextField(blank=True, null=True),
        ),
    ]
