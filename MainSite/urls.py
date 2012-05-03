from django.conf.urls import patterns, include, url
from about.views import about_pages
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^about/(\w+)/$', about_pages),
    (r'^accounts', include('accounts.urls')),
    (r'^$',direct_to_template, {'template':'home.html',}),
    (r'^auth', include('auth.urls')),

    # Examples:s
    # url(r'^$', 'MainSite.views.home', name='home'),
    # url(r'^MainSite/', include('MainSite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
