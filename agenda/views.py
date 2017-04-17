from django.views.generic import TemplateView, CreateView, UpdateView
from django.views.generic.edit import FormView, CreateView
from django.core.urlresolvers import reverse_lazy
from models import Contatos, Tag
from forms import Agenda, DynamicForm

# Create your views here.


class Index(TemplateView):
    template_name = "agenda/index.html"

index = Index.as_view()


class ContactAdd(CreateView):
    model = Contatos
    fields = ['nome']
    success_url = reverse_lazy('add-contato')

addcontact = ContactAdd.as_view()


class EditContact(UpdateView):
    model = Contatos
    fields = ['nome']

    def get_sucess_url(self):
        return reverse_lazy('edit-contato', {'pk': self.__id})

editcontato = EditContact.as_view()


class Test(FormView):
    template_name = "agenda/teste.html"
    form_class = DynamicForm
    success_url = reverse_lazy('teste')

    def form_valid(self, form):
        tags = []
        for i in form.cleaned_data['tag'].split(','):
            tag, created = Tag.objects.get_or_create(nome=i)
            tags.append(tag.pk)
        form.cleaned_data['tag'] = tags
        return super(Test, self).form_valid(form)
