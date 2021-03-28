from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView, RedirectView

from core.forms import AddUrlForm
from core.helpers import create_url_instance, get_redirect_url
from core.models import Url


class HomePageView(ListView):
    model = Url
    context_object_name = 'urls'
    paginate_by = 5

    def post(self, request, *args, **kwargs):
        add_url_form = AddUrlForm(request.POST or None)
        context = self.get_context_data(object_list=self.get_queryset())
        if not add_url_form.is_valid():
            messages.error(self.request, add_url_form.errors)
            return redirect('core:home-page')
        validated_data = add_url_form.cleaned_data
        new_url = create_url_instance(request, validated_data)
        context['url_subpart'] = new_url.url_subpart
        return render(request=request, template_name='core/url_list.html', context=context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_url_form'] = AddUrlForm()
        return context

    def get_queryset(self):
        return self.model.objects.filter(session_id=self.request.session.session_key).order_by('-created_at')


class RedirectUrlPage(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        url = get_redirect_url(kwargs['url_subpart'])
        return url
