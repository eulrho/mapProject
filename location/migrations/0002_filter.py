# Generated by Django 4.0.4 on 2022-06-04 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('E', models.BooleanField(default='True')),
                ('N', models.BooleanField(default='True')),
                ('S', models.BooleanField(default='True')),
            ],
        ),
    ]
