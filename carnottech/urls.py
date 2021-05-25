from django.conf.urls import url
from carnottech import views
from django.urls import path

urlpatterns=[
    url(r'^$',views.home, name='home'),
    url(r'^fetch',views.fetch, name='fetch')
]