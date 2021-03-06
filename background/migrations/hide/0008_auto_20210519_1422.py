# Generated by Django 3.2.2 on 2021-05-19 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20210519_1422'),
        ('background', '0007_alter_flight_flight_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight',
            name='flight_type',
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_number', models.AutoField(primary_key=True, serialize=False, verbose_name='订单编号')),
                ('price', models.FloatField(verbose_name='机票价格')),
                ('order_time', models.DateTimeField(auto_now_add=True, verbose_name='订单创建时间')),
                ('seat_number', models.IntegerField(verbose_name='座位号')),
                ('flight_type', models.CharField(choices=[('4', '经济舱'), ('1', '头等舱'), ('3', '商务舱'), ('2', '高端经济舱')], max_length=1, verbose_name='舱位类型')),
                ('Id_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.user', verbose_name='身份证号')),
                ('flight_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='background.flight', verbose_name='航班号')),
            ],
        ),
    ]
