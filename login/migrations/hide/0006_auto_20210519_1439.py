# Generated by Django 3.2.2 on 2021-05-19 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20210519_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='flight_mileage',
            field=models.FloatField(default=0, verbose_name='飞行里程'),
        ),
        migrations.AddField(
            model_name='user',
            name='total_consumption',
            field=models.FloatField(default=0, verbose_name='消费总额'),
        ),
        migrations.AlterField(
            model_name='user',
            name='credit_rating',
            field=models.CharField(choices=[('1', 'C'), ('3', 'A'), ('5', 'AAA'), ('2', 'B'), ('4', 'AA')], default='3', max_length=10, verbose_name='信用等级'),
        ),
    ]
