# Generated by Django 4.2.16 on 2024-10-21 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='credit',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='name',
            field=models.CharField(default=11, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='semester',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
