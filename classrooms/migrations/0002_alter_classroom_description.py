# Generated by Django 4.1.1 on 2022-09-06 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classrooms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
