from django.conf.urls import patterns, url
from accounts.views import AccountListView, JSONAccountListView, XMLAccountListView , AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView, JSONAccountDetailView, XMLAccountDetailView


urlpatterns = patterns('',
    url(r'^.json$',JSONAccountListView.as_view(),name='json_account_list'),
    url(r'^.xml$',XMLAccountListView.as_view(),name='xml_account_list'),
    url(r'^$',AccountListView.as_view(),name='account_list'),
    url(r'^/create$',AccountCreateView.as_view(),name='account_create'),
    url(r'^/(?P<pk>\d+).json$', JSONAccountDetailView.as_view(),name='json_account_detail'),
    url(r'^/(?P<pk>\d+).xml$', XMLAccountDetailView.as_view(),name='xml_account_detail'),
    url(r'^/(?P<pk>\d+)$', AccountDetailView.as_view(),name='account_detail'),
    url(r'^/(?P<pk>\d+)/edit$', AccountUpdateView.as_view(),name='account_edit'),
    url(r'^/(?P<pk>\d+)/delete$', AccountDeleteView.as_view(),name='account_delete'),
)
