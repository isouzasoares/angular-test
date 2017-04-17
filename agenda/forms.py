from django import forms
from models import Contatos


class Agenda(forms.ModelForm):

    tag = forms.CharField()

    class Meta:
        model = Contatos
        fields = '__all__'


class DynamicForm(forms.Form):
    test = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(DynamicForm, self).__init__(*args, **kwargs)
        extras = [{'name': 'name',
                   'type': 'CharField',
                   'kwargs': {'label': 'label_do_name', 'required': True} }]
        for extra in extras:
            self.fields[extra['name']] = getattr(forms, extra['type'])(**extra['kwargs'])
