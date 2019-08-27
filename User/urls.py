from django.conf.urls import url

from . import views as user_views

urlpatterns = [

    url(r'^$', user_views.user_login, name='user_login'),
    url(r'^register/', user_views.user_register, name='register')
]