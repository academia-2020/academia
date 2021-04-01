# Generated by Django 3.1.7 on 2021-03-26 20:33

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20210325_1916'),
        ('visitante', '0003_auto_20210326_1809'),
    ]

    operations = [
        migrations.CreateModel(
            name='capitulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
                ('descripcion', ckeditor.fields.RichTextField()),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.curso')),
            ],
        ),
        migrations.CreateModel(
            name='tema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
                ('descripcion', ckeditor.fields.RichTextField()),
                ('capitulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitante.capitulo')),
            ],
        ),
    ]
