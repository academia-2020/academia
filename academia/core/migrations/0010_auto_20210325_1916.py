# Generated by Django 3.1.7 on 2021-03-25 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_disciplina'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='disciplina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.disciplina'),
        ),
    ]
