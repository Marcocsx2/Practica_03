from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'api/library/books', views.book_list),
    url(r'api/library/lends', views.lend_list),
    url(r'api/library/users', views.user_list),
    url(r'api/library/lends(?P<pk>[0-9]+)/$', views.lend_detail),
]
