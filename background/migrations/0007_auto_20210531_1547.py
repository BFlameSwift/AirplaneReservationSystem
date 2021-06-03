# Generated by Django 3.2.2 on 2021-05-31 15:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('background', '0006_auto_20210526_0846'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='concrete_flight',
            options={'verbose_name': '具体航班'},
        ),
        migrations.AlterModelOptions(
            name='flightseatingchart',
            options={'verbose_name': '航班座位表'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': '订单', 'verbose_name_plural': '订单信息'},
        ),
        migrations.AlterField(
            model_name='order',
            name='flight_datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 31, 15, 47, 41, 480196), verbose_name='航班飞行具体时间'),
        ),
        migrations.AlterField(
            model_name='order',
            name='flight_type',
            field=models.CharField(choices=[('3', '商务舱'), ('4', '经济舱'), ('2', '高端经济舱'), ('1', '头等舱')], max_length=1, verbose_name='舱位类型'),
        ),
    ]