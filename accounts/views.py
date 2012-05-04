from django import http
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.core import serializers

from django.views.generic.detail import BaseDetailView
from django.views.generic.list import BaseListView

from accounts.forms import AccountForm
from models import Account

class DataResponseMixin(object):
    data_type = 'application/json'
    def render_to_response(self, context):
        "Returns a data response"
        return self.get_data_response(self.convert(context))

    def get_data_response(self, content, **httpresponse_kwargs):
        "Construct an `HttpResponse` object."
        return http.HttpResponse(content,
                                 content_type=self.data_type,
                                 **httpresponse_kwargs)

    def convert(self, context):
        pass


class AccountListView(ListView):
    model = Account
    template_name = 'accounts/account_list.html'

class JSONAccountListView(DataResponseMixin, BaseListView):
    model = Account

    def convert(self, context):
        return serializers.serialize('json', self.get_queryset())


class XMLAccountListView(DataResponseMixin, BaseListView):
    model = Account
    data_type = 'application/xml'

    def convert(self, context):
        return serializers.serialize('xml', self.get_queryset())



class AccountCreateView(CreateView):
    form_class = AccountForm
    model = Account    
    def get_success_url(self):
        return reverse('account_list')
    
class AccountDetailView(DetailView):
    model = Account
            
class JSONAccountDetailView(DataResponseMixin, BaseDetailView):
    model = Account

    def convert(self, context):
        return serializers.serialize('json', [ self.get_object(), ])
        

class XMLAccountDetailView(DataResponseMixin, BaseDetailView):
    model = Account
    data_type = 'application/xml'

    def convert(self, context):
        return serializers.serialize('xml', [ self.get_object(), ])


class AccountUpdateView(UpdateView):
    form_class = AccountForm
    model = Account

    def get_success_url(self):
        return reverse('account_detail',args=[self.get_object().id,])
            
class AccountDeleteView(DeleteView):
    model = Account
    success_url = reverse_lazy('account_list')
