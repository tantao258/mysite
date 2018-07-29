from django.db import models

# Create your models here.

# 小说信息
class NovelInfo(models.Model):
    website = models.CharField(max_length=100, null=True, db_index=True)
    book_name = models.CharField(max_length=100, null=True, db_index=True)
    author = models.CharField(max_length=100, null=True, db_index=True)
    total_words = models.IntegerField(null=True, db_index=True)
    category = models.CharField(max_length=100, null=True, db_index=True)
    tags = models.CharField(max_length=100, null=True, db_index=True)
    review_times = models.IntegerField(null=True, db_index=True)
    click_times = models.IntegerField(null=True, db_index=True)
    popularity = models.IntegerField(null=True, db_index=True)
    read_times = models.IntegerField(null=True, db_index=True)
    collection_times = models.IntegerField(null=True, db_index=True)
    book_url = models.CharField(max_length=100, null=True, db_index=True)
    image = models.CharField(max_length=100, null=True, db_index=True)

    # # 外键
    source = models.ForeignKey(to="NovelSource", to_field="uid", on_delete=models.CASCADE, default=1)


class NovelSource(models.Model):
    uid = models.AutoField(primary_key=True)  # 主键
    website = models.CharField(max_length=100, null=True, db_index=True)