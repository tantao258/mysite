from django.db import models

"""
Django数据库数据类型：字符串、数字、时间
http://www.cnblogs.com/wupeiqi/articles/5246483.html
自增（primary_key=True）
null 字段是否可以为空
default 默认值
primary_key 主键
db_column 列名
db_index 该字段可以被索引    db_index=True
unique   唯一索引
unique_for_date    -> 
unique_for_month
unique_for_year
auto_now           -> 创建时，自动生成时间
    create_time = models.DateTimeField(auto_now_add=True, null=True)
auto_now_add       -> 更新时，自动更新为当前时间
    updata_time = models.DateTimeField(auto_now=True, null=True)
        # 该方法更新时间不生效
        # obj = UserGroup.objects.filter(id=1).update(caption='CEO') 
        # 该方法更新时间才生效  
        # obj = UserGroup.objects.filter(id=1).first()
        # obj.caption = "CEO"
        # obj.save()

"""
# Create your models here.
# 更新数据表都要运行
# python manage.py makemigrations
# python manage.py migrate


class UserGroup(models.Model):
    # 创建自增列
    uid = models.AutoField(primary_key=True)  # 主键
    group = models.CharField(max_length=16, null=True, db_index=True)


# 通过创建类来创建数据库
# 表名： app05_mysql_userinfo
class UserInfo(models.Model):
    # 自动创建ID列，自增，主键
    # 用户名列，字符串类型， 指定长度
    username = models.CharField(max_length=32, null=True, db_index=True)
    # 密码，字符串类型， 指定长度
    password = models.CharField(max_length=64, null=True)
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, null=True)
    update_time = models.DateTimeField(auto_now=True, null=True)
    # 年龄， 数字类型，指定长度
    # age = models.IntegerField(max_length=3, null=True)
    # 在已有数据的数据表上增加一列 邮箱
    # email = models.CharField(max_length=60, null=True)
    # 注释掉某一列后更新数据表则删除该字段

    # 外键
    user_group = models.ForeignKey(to="UserGroup", to_field="uid", on_delete=models.CASCADE, default=1)
    # models.UserInfo.objects.all()[i].user_group_id
    # models.UserInfo.objects.all()[i].user_group
    # user_group  --> UserGroup 的对象(uid, group)
    # 获取数据 usergroup.uid     usergroup.group






