# Generated by Django 3.2.2 on 2021-06-03 20:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('background', '0008_auto_20210603_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='concrete_flight',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='background.concrete_flight', verbose_name='具体航班'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='flight_datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 3, 20, 18, 19, 641468), verbose_name='航班飞行具体时间'),
        ),
        migrations.AlterField(
            model_name='order',
            name='flight_type',
            field=models.CharField(choices=[('1', '头等舱'), ('3', '商务舱'), ('2', '高端经济舱'), ('4', '经济舱')], max_length=1, verbose_name='舱位类型'),
        ),
    ]