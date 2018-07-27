from django.db import models

# Create your models here.

# 用户等级数据表
class UserLevel(models.Model):
    uid = models.AutoField(primary_key=True)   # 主键
    level = models.CharField(max_length=16, null=True, db_index=True)

# 用户信息
class UserInfo(models.Model):
    username = models.CharField(max_length=32, null=True, db_index=True)
    password = models.CharField(max_length=64, null=True)
    telephone = models.CharField(max_length=11, null=True, db_index=True)
    email = models.CharField(max_length=32, null=True, db_index=True)
    # 外键
    user_level = models.ForeignKey(to="UserLevel", to_field="uid", on_delete=models.CASCADE, default=3)