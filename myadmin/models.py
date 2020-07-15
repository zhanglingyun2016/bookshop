from django.db import models

# Create your models here.
"""
创建模型，数据迁移
python manage.py makemigrations
python manage.migrate
"""

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=160)
    phone = models.CharField(max_length=20)
    sex = models.CharField(max_length=11)
    age = models.CharField(max_length=11)
    addtime = models.CharField(max_length=50)
    logintime = models.CharField(max_length=50)
    status = models.CharField(max_length=500)





# 图书分类模型
class Booktype(models.Model):
    name = models.CharField(max_length=10)
    pid = models.IntegerField()  #父级
    path = models.CharField(max_length=50)




# 图书商品模型
class Books(models.Model):
    title = models.CharField(max_length=255)
    tuijian = models.CharField(max_length=255)
    author = models.CharField(max_length=50)
    publisher = models.CharField(max_length=100)   #出版商
    pub_date = models.CharField(max_length=50)
    price = models.FloatField()
    num = models.IntegerField(default=10)  #库存数量
    isbn = models.CharField(max_length=13)
    context = models.TextField()


# 图书商品封面模型
class BookImg(models.Model):
    bookid = models.ForeignKey("Books",on_delete=models.CASCADE)
    img_url = models.CharField(max_length=100)
















