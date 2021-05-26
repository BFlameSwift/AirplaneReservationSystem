import datetime

from django.db import models
from login.models import User

# Create your models here.

class Flight(models.Model):
    flight_number = models.CharField(max_length=32, primary_key=True, verbose_name="航班号")

    plane_type_choices = [
        ('波音', (
            ('1', '747'),
            ('2', '777'),
            ('3', '787'),
        )
         ),
        ('空客', (
            ('4', 'A300'),
            ('5', 'A310'),
            ('6', 'A320'),
            ('7', 'A350'),
        )
         ),
    ]
    origination = models.CharField(max_length=32, verbose_name="始发地")
    destination = models.CharField(max_length=32, verbose_name="目的地")
    departure_airport = models.CharField(max_length=64,verbose_name="始发机场")
    landing_airport = models.CharField(max_length=64,verbose_name="目的机场")

    starting_time = models.TimeField(verbose_name="始发时间", blank=False)
    flight_time = models.TimeField(verbose_name="飞行时间",blank=True)
    arrival_time = models.TimeField(verbose_name="到达时间", blank=False)
        
    first_class_price = models.FloatField(verbose_name="头等舱价格",default=2000)
    highlevel_economy_class_price = models.FloatField(verbose_name="经济舱价格", default=1500)
    business_class_price = models.FloatField(verbose_name="商务舱价格",default=1000)
    economy_class_price = models.FloatField(verbose_name="经济舱价格",default=500)

    book_sum = models.IntegerField(verbose_name="订票总数",default=0)
    plane_type = models.CharField(verbose_name="飞机型号", max_length=30, choices=plane_type_choices)
    plane_capacity = models.IntegerField(verbose_name="飞机容量", blank=True)


    # class Meta:
    # db_table = 'flight'
    class Meta:
        verbose_name ='航班信息'
        verbose_name_plural = '航班信息'
    # 基本约束还没添加
    #     constraints = [
    #         models.CheckConstraint(check=models.)
    #
    #     ]



    # 座位号与flight_id 决定 对应一个航班，（如果使用外键上下两个类互相外键无法引用
    #


class Concrete_flight(models.Model):
    # 由于航班的可重复性，把航班的时间设置成time格式， 但是需要每天的一个独立航班来有单次航班的预订次数
    id = models.AutoField(primary_key=True)
    flight = models.ForeignKey(Flight,verbose_name="航班",on_delete=models.CASCADE)
    book_sum = models.IntegerField(verbose_name="订票总数", default=0)
    plane_capacity = models.IntegerField(verbose_name="飞机容量", blank=True) # 冗余列，方便起见
    flight_datetime = models.DateTimeField(verbose_name="航班时间")
    # seat_chart = models.ForeignKey(FlightSeatingChart,on_delete=models.CASCADE,verbose_name="座位表",)
    class Meta:
        verbose_name ='具体航班'
    # 利用
class FlightSeatingChart(models.Model):
    # 座位表，每一天的每一个航班都有一个，否则数组比较难实现，
    # 以此来安排座位.(根据订票数来确定座位存在 bug
    id = models.AutoField(primary_key=True)
    seat_number = models.IntegerField(unique=False, verbose_name="座位号")
    concrete_flight = models.ForeignKey(Concrete_flight,verbose_name="具体航班",on_delete=models.CASCADE)
    # user = models.ForeignKey(User,verbose_name="用户",on_delete=models.CASCADE)
    is_occupied = models.BooleanField(default=False,verbose_name="该座位是否被占用")
    class Meta:
        verbose_name ='航班座位表'

class Order(models.Model):
    order_number = models.AutoField(primary_key=True,verbose_name = "订单编号")
    flight = models.ForeignKey(Flight,verbose_name="航班",on_delete=models.CASCADE)
    # flight_date = models.DateField(verbose_name="航班飞行日期")
    flight_datetime = models.DateTimeField(verbose_name="航班飞行具体时间",default=datetime.datetime.now())
    user = models.ForeignKey(User,verbose_name="用户",on_delete=models.CASCADE)
    price = models.FloatField(verbose_name="机票价格")
    order_time = models.DateTimeField(auto_now_add=True,verbose_name="订单创建时间")
    seat_number = models.IntegerField(verbose_name="座位号",)

    order_is_valid = models.BooleanField(verbose_name="订单是否有效",default=True)
    luggage_weight = models.FloatField(verbose_name="行李重量",default=0)
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
    class Meta:
        verbose_name ='订单'
        verbose_name_plural = '订单信息'

    # class Meta:
        # da_table = 'order'







    #飞机容量可随飞机型号的设定而自动设定



