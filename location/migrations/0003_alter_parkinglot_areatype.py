# Generated by Django 4.0.4 on 2022-06-04 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_filter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkinglot',
            name='areatype',
            field=models.CharField(choices=[('E', 'E구역'), ('N', 'N구역'), ('S', 'S구역'), ('etc', '기타')], default='E', max_length=200),
        ),
    ]
