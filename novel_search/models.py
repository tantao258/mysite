from django.db import models

# Create your models here.

# 小说信息
class NovelInfo(models.Model):
    website = models.CharField(max_length=100, null=True, db_index=True)
    book_name = models.CharField(max_length=100, null=True, db_index=True)
    author = models.CharField(max_length=100, null=True, db_index=True)
    total_words = models.CharField(max_length=100, null=True, db_index=True)
    category = models.CharField(max_length=100, null=True, db_index=True)
    tags = models.CharField(max_length=100, null=True, db_index=True)
    review_times = models.CharField(max_length=100, null=True, db_index=True)
    click_times = models.CharField(max_length=100, null=True, db_index=True)
    popularity = models.CharField(max_length=100, null=True, db_index=True)
    read_times = models.CharField(max_length=100, null=True, db_index=True)
    collection_times = models.CharField(max_length=100, null=True, db_index=True)
    book_url = models.CharField(max_length=100, null=True, db_index=True)
    image = models.CharField(max_length=100, null=True, db_index=True)

    # 外键
    # user_level = models.ForeignKey(to="UserLevel", to_field="uid", on_delete=models.CASCADE, default=3)
