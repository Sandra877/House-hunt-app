# Generated by Django 5.0.2 on 2024-02-11 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='plansmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.TextField()),
                ('price', models.FloatField()),
                ('promotions', models.CharField(max_length=150)),
            ],
        ),
    ]
