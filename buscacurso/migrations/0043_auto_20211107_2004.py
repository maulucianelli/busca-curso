# Generated by Django 3.2.6 on 2021-11-07 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buscacurso', '0042_alter_coursesdescription_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='CoursesDescription',
        ),
    ]