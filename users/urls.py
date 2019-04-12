# users/urls.py
 
from django.conf.urls import url
from users.views import LoginUser, CreateUser, LoginUser, UserRetrieveUpdateAPIView
 
urlpatterns = [
    url(r'^create/$', CreateUser.as_view()),
    url(r'^login/$', LoginUser.as_view()),
    url(r'^update/$', UserRetrieveUpdateAPIView.as_view()),

]