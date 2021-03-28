from django import forms

from core.models import Url


class AddUrlForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddUrlForm, self).__init__(*args, **kwargs)
        self.fields['url_subpart'].required = False

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
