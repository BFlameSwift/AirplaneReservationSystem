import datetime

from django.db import models

# Create your models here.1


class User(models.Model):

    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    rate = {
        ('5','AAA'),
        ('4','AA'),
        ('3','A'),
        ('2','B'),
        ('1','C'),
    }
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, unique=True,verbose_name="用户名")
    password = models.CharField(max_length=256,verbose_name="密码")
    email = models.EmailField(unique=True,verbose_name="邮箱")
    sex = models.CharField(max_length=32, choices=gender, default="男",verbose_name="邮箱")
    register_time = models.DateTimeField(auto_now_add=True)
    last_login_time = models.DateTimeField(verbose_name="上次登录时间",blank=True,default=datetime.datetime.now())
    has_confirmed = models.BooleanField(default=False,verbose_name="是否已经邮箱验证")
    Id_number = models.CharField(max_length=20,unique=True,verbose_name="身份证号",blank=True)
    credit_rating = models.CharField(max_length=10,choices=rate,default='B',verbose_name="信用等级")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-register_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"


class ConfirmString(models.Model):
    code = models.CharField(max_length=256)
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name + ":   " + self.code

    class Meta:

        ordering = ["-c_time"]
        verbose_name = "确认码"
        verbose_name_plural = "确认码"