# Generated by Django 3.2.2 on 2021-05-18 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('background', '0005_auto_20210517_1559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight',
            name='flight_price',
        ),
        migrations.AddField(
            model_name='flight',
            name='book_sum',
            field=models.IntegerField(default=0, verbose_name='订票总数'),
        ),
        migrations.AddField(
            model_name='flight',
            name='business_class_price',
            field=models.FloatField(default=1000, verbose_name='商务舱价格'),
        ),
        migrations.AddField(
            model_name='flight',
            name='economy_class_price',
            field=models.FloatField(default=500, verbose_name='经济舱价格'),
        ),
        migrations.AddField(
            model_name='flight',
            name='first_class_price',
            field=models.FloatField(default=2000, verbose_name='头等舱价格'),
        ),
        migrations.AddField(
            model_name='flight',
            name='highlevel_economy_class_price',
            field=models.FloatField(default=1500, verbose_name='经济舱价格'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='flight_type',
            field=models.CharField(choices=[('1', '头等舱'), ('2', '高端经济舱'), ('4', '经济舱'), ('3', '商务舱')], default='经济舱', max_length=1, verbose_name='航班类型'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='plane_type',
            field=models.CharField(choices=[('波音', (('1', '747'), ('2', '767'), ('3', '777'))), ('空客', (('4', 'A300'), ('5', 'A310'), ('6', 'A320'), ('7', 'A340')))], max_length=30, verbose_name='飞机型号'),
        ),
    ]
