from django.conf.urls import url
from first_app import views
from django.core.urlresolvers import reverse_lazy

urlpatterns = [
    url(r'^$',views.index,name='index'),
]
