from django.conf.urls import url
from . import views

app_name = 'Post'
urlpatterns = [
    url(r'^$',views.all_post,name='all_post'),
    url(r'^(?P<id>\d+)$' , views.post ,name='post')
]
