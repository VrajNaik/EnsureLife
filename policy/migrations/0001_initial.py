# Generated by Django 3.1.5 on 2021-02-13 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_name', models.CharField(max_length=50)),
                ('high_premium', models.BooleanField()),
                ('accidental_cover', models.BooleanField()),
                ('surrender_value', models.BooleanField()),
                ('market_risk', models.BooleanField()),
                ('age_group', models.CharField(max_length=50)),
                ('term_period', models.CharField(max_length=50)),
                ('premium_wavier', models.BooleanField()),
                ('maturity', models.CharField(max_length=50)),
            ],
        ),
    ]
