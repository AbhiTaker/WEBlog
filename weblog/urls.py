from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^diary',views.diary, name='diary'),
    url(r'^about',views.about, name='about'),
    url(r'^write',views.write, name='write'),

]
