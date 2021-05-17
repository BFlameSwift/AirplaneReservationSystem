# Generated by Django 3.2.2 on 2021-05-17 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('background', '0004_auto_20210517_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='flight_type',
            field=models.CharField(choices=[('3', '商务舱'), ('2', '高端经济舱'), ('1', '头等舱'), ('4', '经济舱')], default='经济舱', max_length=1, verbose_name='航班类型'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='plane_capacity',
            field=models.IntegerField(blank=True, verbose_name='飞机容量'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='plane_type',
            field=models.CharField(choices=[('波音', (('1', '747'), ('2', '767'), ('3', '777'))), ('空客', (('4', '300'), ('5', '310'), ('6', '320'), ('7', '340')))], max_length=30, verbose_name='飞机型号'),
        ),
    ]