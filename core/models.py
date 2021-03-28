from django.contrib.sessions.models import Session
from django.core.validators import RegexValidator
from django.db import models


class Url(models.Model):
    session = models.ForeignKey(Session, on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='Session пользователя')
    original_url = models.URLField(verbose_name='Оригинальный URL')
    url_subpart = models.CharField(unique=True,
                                   max_length=32,
                                   validators=[
                                       RegexValidator(regex='^.{3,32}$',
                                                      message='Subpart has to be at least 3 characters long',
                                                      code='nomatch')],
                                   verbose_name='URL subpart')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.original_url} -> {self.url_subpart}'
