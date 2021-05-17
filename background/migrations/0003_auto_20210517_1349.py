# Generated by Django 3.2.2 on 2021-05-17 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('background', '0002_alter_flight_flight_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='flight_time',
            field=models.CharField(blank=True, max_length=20, verbose_name='飞行时间'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='flight_type',
            field=models.CharField(choices=[('3', '商务舱'), ('4', '经济舱'), ('2', '高端经济舱'), ('1', '头等舱')], default='经济舱', max_length=1, verbose_name='航班类型'),
        ),
    ]