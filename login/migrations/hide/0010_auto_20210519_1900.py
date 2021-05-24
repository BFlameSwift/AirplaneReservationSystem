# Generated by Django 3.2.2 on 2021-05-19 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_auto_20210519_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default=1, max_length=32, unique=True, verbose_name='手机号码'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='credit_rating',
            field=models.CharField(choices=[('3', 'A'), ('5', 'AAA'), ('1', 'C'), ('4', 'AA'), ('2', 'B')], default='3', max_length=10, verbose_name='信用等级'),
        ),
    ]