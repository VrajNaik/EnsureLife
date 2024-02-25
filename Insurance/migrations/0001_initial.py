# Generated by Django 3.1.5 on 2021-01-29 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_name', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='assets/images')),
                ('sum', models.IntegerField()),
                ('description', models.CharField(max_length=500000)),
                ('premium', models.IntegerField()),
                ('no', models.IntegerField()),
                ('loan', models.BooleanField()),
            ],
        ),
    ]