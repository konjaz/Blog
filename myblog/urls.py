from django.conf.urls import url
from . import views
from .views import post_list_api, PostData, PostList

urlpatterns = [
    url(r'^$', PostList.as_view(), name='home'),
    url(r'^api/posts/$', post_list_api, name='api-posts'),
    url(r'^api/post/data/$', PostData.as_view(), name='api-post-data'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]