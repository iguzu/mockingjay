# import datetime
from django.contrib.auth.decorators import login_required
from django import http
from django.core.urlresolvers import reverse_lazy, reverse
# from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.core import serializers

from django.views.generic.detail import BaseDetailView
from django.views.generic.list import BaseListView

from accounts.forms import AccountForm
from models import Account
from django.utils.decorators import method_decorator


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
#    queryset = queryset=Account.objects.order_by("name")
    template_name = 'accounts/account_list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AccountListView, self).dispatch(*args, **kwargs)

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
    success_url = reverse_lazy('account_list')
    
class AccountDetailView(DetailView):
    model = Account
#    def get(self,*args,**kwargs):
#        if 'pk' in kwargs:
#            my_object = get_object_or_404(Account, pk=kwargs['pk'])
#            my_object.last_accessed = datetime.datetime.now()
#            my_object.save()
            
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
