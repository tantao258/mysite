from django.db import models

"""
Django数据库数据类型：字符串、数字、时间
"""
# Create your models here.

# 通过创建类来创建数据库
# 表名： app05_mysql_userinfo
class UserInfo(models.Model):

    # 用户名列，字符串类型， 指定长度
    username = models.CharField(max_length=32)
    # 密码，字符串类型， 指定长度
    password = models.CharField(max_length=64)
    # 自动创建ID列，自增，主键


