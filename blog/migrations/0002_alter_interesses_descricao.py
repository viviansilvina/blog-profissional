# Generated by Django 5.1 on 2024-08-24 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interesses',
            name='descricao',
            field=models.TextField(blank=True, null=True),
        ),
    ]
