# Generated by Django 3.2.8 on 2021-10-20 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buscacurso', '0022_coursesinstitution_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintainer',
            name='name',
            field=models.CharField(default='Mantenedora', max_length=200),
        ),
    ]
