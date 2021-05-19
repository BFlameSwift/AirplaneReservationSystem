from django.db import models

# Create your models here.

class Flight(models.Model):
    flight_number = models.CharField(max_length=30, primary_key=True, verbose_name="航班号")
    filght_level = {
            ('1','头等舱'),
            ('2', '高端经济舱'),
            ('3','商务舱'),
            ('4','经济舱')
        }
    plane_type_choices = [
        ('波音', (
            ('1', '747'),
            ('2', '767'),
            ('3', '777'),
        )
         ),
        ('空客', (
            ('4', 'A300'),
            ('5', 'A310'),
            ('6', 'A320'),
            ('7', 'A340'),
        )
         ),
    ]
    flight_type = models.CharField(
        max_length=1,
        choices=filght_level,
        default='经济舱',
        verbose_name="航班类型",
    )
    origination = models.CharField(max_length=30, verbose_name="始发地", blank=False)
    destination = models.CharField(max_length=30, verbose_name="目的地", blank=False)
    starting_time = models.TimeField(verbose_name="始发时间", blank=False)
    flight_time = models.CharField(verbose_name="飞行时间", max_length=20, blank=True)


    arrival_time = models.TimeField(verbose_name="到达时间", blank=False)
    first_class_price = models.FloatField(verbose_name="头等舱价格",default=2000)
    highlevel_economy_class_price = models.FloatField(verbose_name="经济舱价格", default=1500)
    business_class_price = models.FloatField(verbose_name="商务舱价格",default=1000)
    economy_class_price = models.FloatField(verbose_name="经济舱价格",default=500)

    book_sum = models.IntegerField(verbose_name="订票总数",default=0)
    plane_type = models.CharField(verbose_name="飞机型号", max_length=30, choices=plane_type_choices)
    plane_capacity = models.IntegerField(verbose_name="飞机容量", blank=True)

    # class Meta:
    #     constraints = [
    #         models.CheckConstraint(check=models.)
    #
    #     ]









    #飞机容量可随飞机型号的设定而自动设定



