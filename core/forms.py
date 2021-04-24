from django import forms

from core.helpers import get_random_string, get_session_instance
from core.models import Url


class AddUrlForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', '')
        super(AddUrlForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Url
        fields = ('original_url', 'url_subpart')
        labels = {
            'original_url': '',
            'url_subpart': ''
        }
        widgets = {
            'original_url': forms.URLInput(attrs={'placeholder': 'Shorten your link'}),
            'url_subpart': forms.TextInput(attrs={'placeholder': 'Subpart for shortened url'})
        }

    def save(self, commit=True):
        new_url = super(AddUrlForm, self).save(commit=False)

        url_subpart = new_url.url_subpart
        while not url_subpart:
            url_subpart = get_random_string()
            if Url.objects.filter(url_subpart=url_subpart).count() > 0:
                url_subpart = ''
            else:
                new_url.url_subpart = url_subpart
        new_url.session = get_session_instance(self.request)

        if commit:
            new_url.save()
        return new_url
