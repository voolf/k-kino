from django.db import models
from django.contrib.auth.models import User
import datetime

# from PIL import Image
# from imagekit.models.fields import ImageSpecField
#import imagekit.processors

# Create your models here.

class Film (models.Model):
    class Meta():
        db_table = "film"

    film_name = models.CharField(max_length=300)
    film_created_users = models.TextField(default='-')
    film_genre = models.CharField(max_length=40)
    film_text = models.TextField()
    film_year = models.IntegerField(default=datetime.datetime.today().year)
    film_date_public = models.DateTimeField(default=datetime.datetime.today())
    film_user = models.ForeignKey(User)
    film_award = models.TextField(default='none')
    film_like = models.IntegerField(default=0)
    film_sided_site = models.IntegerField(default=0)# или 0 или 1 или 2 отсутсвует, youtube,vimeo
    film_sided_id = models.CharField(max_length=200)
    film_country = models.CharField(max_length=200)
    film_money_create = models.IntegerField(default=0)



class Film_comment (models.Model):
    class Meta():
        db_table = "film_comment"
    film_comment_date = models.DateTimeField()
    film_comment_text = models.TextField(verbose_name="написать комментарий")
    film_comment_link = models.ForeignKey(Film)
    film_comment_user = models.ForeignKey(User)

