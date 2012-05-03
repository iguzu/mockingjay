from django.conf.urls import patterns, url
from auth.views import LogoutView, LoginView

urlpatterns = patterns('',
    url(r'^/login$', LoginView.as_view(),'auth_login'),
    (r'^/logout$', LogoutView),
)
