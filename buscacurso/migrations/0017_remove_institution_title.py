# Generated by Django 3.2.8 on 2021-10-20 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buscacurso', '0016_alter_institution_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='institution',
            name='title',
        ),
    ]
