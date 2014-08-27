from django.db import models
from django.contrib.auth.models import User
import datetime
import random
#from django.conf import settings
# from PIL import Image
# from imagekit.models.fields import ImageSpecField
#import imagekit.processors

# Create your models here.

class Jenre (models.Model):
    class Meta():
       # db_table = "jenre"
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    jenre_name =     models.CharField(max_length=256, verbose_name="название жанра транслитом")
    jenre_title = models.CharField(max_length=256, verbose_name="Название жанра")

    def __unicode__(self):
        return self.jenre_title #возвращает в место полученого объекта заголовог из базы


class Status (models.Model):
    status_film_name = models.CharField(verbose_name='состояние фильма', max_length=30)
    class Meta():
        verbose_name = 'Статусы'
        verbose_name_plural = 'Статус'
    def __unicode__(self):
        return self.status_film_name

class Film (models.Model):
    class Meta():
        db_table = "film"
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

    film_name = models.CharField(max_length=300)
    film_created_users = models.TextField(default="", blank=True)
    film_jenres = models.ManyToManyField(Jenre, related_name="films", verbose_name=u"Жанр")
    #film_tags = models.ManyToManyField(Tag, related_name="films", verbose_name=u"теги")
    film_text = models.TextField()
    film_year = models.IntegerField(default=datetime.datetime.today().year)
    film_date_public = models.DateTimeField(default=datetime.datetime.today())
    film_user = models.ForeignKey(User, related_name="films", verbose_name="Пользвоатель")
    film_award = models.TextField(default="", blank=True)
    film_like = models.IntegerField(default=0, blank=True, null=True, verbose_name="лайки")
    film_sided_site = models.IntegerField(default=0)# или 0 или 1 или 2 отсутсвует, youtube,vimeo
    film_sided_id = models.CharField(max_length=200)
    film_country = models.CharField(max_length=200)
    film_status = models.ForeignKey(Status, default=2)
    film_money_create = models.IntegerField(default=0, blank=True, null=True)
    film_is_moderator = models.BooleanField(default=False, blank=True)
    film_image = models.ImageField(upload_to="film_photo", default="/media/filmImg/default.jpg", blank=True)

    def __unicode__(self):
        return self.film_name



class Film_comment (models.Model):
    class Meta():
        db_table = "film_comment"
    film_comment_date = models.DateTimeField()
    film_comment_text = models.TextField(verbose_name="написать комментарий")
    film_comment_link = models.ForeignKey(Film)
    film_comment_user = models.ForeignKey(User)


