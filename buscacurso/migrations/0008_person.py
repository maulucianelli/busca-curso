# Generated by Django 3.2.6 on 2021-08-18 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buscacurso', '0007_curso_faculdade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('number', models.IntegerField(null=True)),
                ('date', models.DateField(null=True)),
            ],
        ),
    ]