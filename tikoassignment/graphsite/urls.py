from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    url('^$', views.welcome, name='welcome'),
    url('^graph/', views.graph, name='graph'),
    url(r'^api/joke/$', views.get_joke, name='api-joke'),
    url(r'^login/', login, {'template_name': 'views/login.html'}),
    # url(r'^api/chartdata/$', views.chartsData.as_view()),
]