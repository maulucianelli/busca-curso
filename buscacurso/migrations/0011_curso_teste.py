# Generated by Django 3.2.6 on 2021-09-19 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buscacurso', '0010_auto_20210818_1839'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso_teste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_curso', models.IntegerField(max_length=25)),
                ('codigo_ies', models.IntegerField(max_length=25)),
                ('sigla_ies', models.CharField(max_length=500)),
                ('nome_ies', models.CharField(max_length=500)),
            ],
        ),
    ]