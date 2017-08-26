from django.conf.urls import url
from level2App import views

urlpatterns=[
    url(r'^$',views.index,name='index')
]
