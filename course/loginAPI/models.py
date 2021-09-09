from django.db import models
from django.utils import timezone
from django.utils.html import mark_safe
from .Signals import change_lastname
from django.db.models.signals import post_save, pre_delete


class Users(models.Model):
    # id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=40, default="", verbose_name="نام کاربری")
    user_lastname = models.CharField(max_length=80, default="")
    user_photo = models.ImageField(upload_to='media', null=True, blank=True)
    user_addres = models.TextField(max_length=400, default="")
    user_phone = models.IntegerField(default=912)
    user_valid_key = models.CharField(default="0", max_length=6)

    def __str__(self):
        return str(self.user_name)

    class Meta:
        verbose_name = "کاربرهای وبسایت"

    def save(self, *args, **kwargs):
        self.user_lastname = self.user_name
        post_save.connect(change_lastname, self)
        super(Users, self).save(*args, **kwargs)


class Token(models.Model):
    token = models.CharField(max_length=40, default="")
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.token


class Brands(models.Model):
    name = models.TextField(default="bb")

    def __str__(self):
        return str(self.id)


class Book(models.Model):
    name = models.CharField(default="", max_length=100)
    # author = models.CharField(default="",max_length=200)
    author_fk = models.ForeignKey(Users, on_delete=models.CASCADE, default=1)
    brand_one = models.OneToOneField(to=Brands, on_delete=models.DO_NOTHING, related_name="one_rel", null=True,
                                     blank=True)
    manyfield = models.ManyToManyField(Users, related_name="many")
    price = models.FloatField(default=0)
    pages = models.IntegerField(default=100)
    photo = models.ImageField(upload_to='books', blank=True, null=True)
    choise_element = (("T", "تایید شده"), ("N", "تایید نشده"), ("P", "منتظر تایید"))
    cofirm = models.CharField(choices=choise_element, default="P", max_length=30)

    datetime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.id)

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.photo))

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True


class Comment(models.Model):
    name = models.CharField(default="", max_length=100)
    email = models.EmailField()
    datetime = models.DateTimeField(default=timezone.now)
    text = models.TextField(default="no comment", max_length=500)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return str(self.id)
