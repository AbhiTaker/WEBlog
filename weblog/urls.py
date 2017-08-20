from django.conf.urls import url

from . import views

urlpatterns = [
	#url(r'^$', views.PostView.as_view(), name='post'),
    #url(r'^$', views.index, name='index'),
    url(r'^$',views.home, name='home'),
    url(r'^diary',views.diary, name='diary'),
    url(r'^about',views.about, name='about'),
    url(r'^write',views.write, name='write'),
    url(r'^read',views.read, name='read'),

]
