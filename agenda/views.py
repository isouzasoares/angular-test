from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class Index(TemplateView):
    template_name = "agenda/index.html"


index = Index.as_view()
