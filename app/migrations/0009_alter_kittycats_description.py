# Generated by Django 3.2.7 on 2021-11-15 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_kittycats_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kittycats',
            name='description',
            field=models.CharField(max_length=20500),
        ),
    ]