from crispy_forms.helper import FormHelper #@UnresolvedImport
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder, Div, HTML, Field #@UnresolvedImport

from django.core.urlresolvers import reverse
import logging
from django.forms import ModelForm
from accounts.models import Account

class AccountForm(ModelForm):
    class Meta:
        model = Account
        exclude = ('date_created','date_last_accessed','date_last_modified',)

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-accountForm'
#        self.helper.form_method = 'post'
#        self.helper.form_action = ''
#        self.helper.form_class = 'form-horizontal'
        logging.critical('test')
        instance = kwargs.get('instance')    
        if instance:
            submit = Submit('submit', 'Update', css_class='btn-primary')
            cancel = HTML(' or <a href="%s">Cancel</a>' % reverse('account_detail', args=[instance.id]))
        else:
            submit = Submit('submit', 'Create', css_class='btn-primary')
            cancel = HTML(' or <a href="%s">Cancel</a>' % reverse('account_list'))
 
        self.helper.layout = Layout(
            Fieldset(
                'Information',
                Div(Div(
                        Field('name',css_class='input-xlarge'),
                        'username',
                        'password',
                        css_class='span8'),
                    Div(HTML('<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam lacus tellus, lobortis sed accumsan quis, ultricies vitae sapien. Sed in dignissim neque. Integer at erat quis libero consequat dictum. Fusce pulvinar leo adipiscing turpis condimentum venenatis.</p>'),css_class='span4'),
                    css_class='row',
                ),                
            ),
            ButtonHolder(
                submit,
                cancel,
            )
        )
           
        super(AccountForm, self).__init__(*args, **kwargs)
        logging.critical(kwargs)
        logging.critical(self.instance)
