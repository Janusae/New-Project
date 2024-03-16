from django.db import models

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=50 , verbose_name="سربرگ محصول")
    name = models.CharField(max_length=50 , verbose_name="نام محصول")
    price = models.IntegerField(verbose_name="قیمت محصول")
    description = models.TextField(verbose_name="توضیحات درباره محصول")
    image = models.ImageField(upload_to="media" , verbose_name="تصویر محصول")
    def __str__(self):
        return f"{self.title}"
    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"
def get_default_id():
    return Products.objects.get(id=1)
class Comment(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, default=get_default_id)
    auther = models.CharField(max_length=50 , verbose_name="نام فرستنده")
    text = models.TextField(max_length=500 ,verbose_name="نظر")
    date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ارسال")