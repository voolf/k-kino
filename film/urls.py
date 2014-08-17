from django.conf.urls import patterns, include, url




urlpatterns = patterns('',

    url(r'^addfilm', 'film.views.filmAdd'),
    url(r'^get/(\d+)/users', 'film.views.filmUsers'),
    url(r'^get/(\d+)', 'film.views.film'),

    #url(r'^articles/all$', 'article.views.articles'),

    #url(r'^articles/like/(?P<article_id>\d+)', 'article.views.like'),
    url(r'^', 'film.views.films'),


)
