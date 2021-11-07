# Generated by Django 3.2.6 on 2021-11-07 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buscacurso', '0034_alter_coursesinstitution_duration'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoursesDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buscacurso.courses')),
            ],
        ),
    ]
