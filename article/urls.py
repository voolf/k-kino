from django.conf.urls import patterns, include, url




urlpatterns = patterns('',

    url(r'^3/', 'article.views.template_three'),
    url(r'^articles/all$', 'article.views.articles'),
    url(r'^articles/get/(\d+)/(\d+)', 'article.views.article'),
    url(r'^articles/get/(\d+)', 'article.views.article'),
    url(r'^articles/addarticle', 'article.views.addArticle'),
    url(r'^articles/editarticle/(\d+)', 'article.views.editArticle'),
    url(r'^articles/like/(?P<article_id>\d+)', 'article.views.like'),
    url(r'^articles/addcomment/(?P<article_id>\d+)', 'article.views.addComment'),
    url(r'^page/(\d+)','article.views.articles'),
    url(r'^', 'article.views.articles'),


)
