# Generated by Django 3.1.6 on 2021-02-19 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Insurance', '0002_auto_20210219_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='insurance',
            name='benefits1',
            field=models.CharField(default=0, max_length=50000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='insurance',
            name='benefits2',
            field=models.CharField(default=0, max_length=50000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='insurance',
            name='info',
            field=models.CharField(default=0, max_length=50000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='insurance',
            name='optbenefits',
            field=models.CharField(default=0, max_length=50000),
            preserve_default=False,
        ),
    ]
