# Generated by Django 3.2.2 on 2021-05-22 14:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0013_auto_20210520_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='real_name',
            field=models.CharField(blank=True, max_length=128, verbose_name='真实姓名'),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(blank=True, default=datetime.date(2021, 5, 22), verbose_name='生日'),
        ),
        migrations.AlterField(
            model_name='user',
            name='credit_rating',
            field=models.CharField(choices=[('2', 'B'), ('5', 'AAA'), ('1', 'C'), ('4', 'AA'), ('3', 'A')], default='3', max_length=10, verbose_name='信用等级'),
        ),
    ]
