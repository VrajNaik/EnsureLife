# Generated by Django 3.1.6 on 2021-03-12 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_auto_20210312_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='done',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
