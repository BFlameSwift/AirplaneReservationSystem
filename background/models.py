from django.db import models
from login.models import User

# Create your models here.

class Flight(models.Model):
    flight_number = models.CharField(max_length=30, primary_key=True, verbose_name="航班号")

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

class Order(models.Model):
    order_number = models.AutoField(primary_key=True,verbose_name = "订单编号")
    flight_number = models.ForeignKey(Flight,verbose_name="航班号",on_delete=models.CASCADE)
    Id_number = models.ForeignKey(User,verbose_name="身份证号",on_delete=models.CASCADE)
    price = models.FloatField(verbose_name="机票价格")
    order_time = models.DateTimeField(auto_now_add=True,verbose_name="订单创建时间")
    seat_number = models.IntegerField(verbose_name="座位号",)
    order_is_valid = models.BooleanField(verbose_name="订单是否有效",default=True)
    #购买成功时生成订单，退订机票时为失效

    filght_level = {
        ('1', '头等舱'),
        ('2', '高端经济舱'),
        ('3', '商务舱'),
        ('4', '经济舱')
    }
    flight_type = models.CharField(
        max_length=1,
        choices=filght_level,
        # default='经济舱',
        verbose_name="舱位类型",
    )










    #飞机容量可随飞机型号的设定而自动设定



