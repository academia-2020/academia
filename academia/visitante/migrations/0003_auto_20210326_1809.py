# Generated by Django 3.1.7 on 2021-03-26 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitante', '0002_recomendacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recomendacion',
            name='nivel',
            field=models.CharField(default='m', max_length=10),
        ),
    ]
