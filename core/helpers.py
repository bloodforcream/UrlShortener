import logging
import random
import string

import redis
from django.contrib.sessions.models import Session
from django.shortcuts import get_object_or_404

from core.models import Url

logger = logging.getLogger(__name__)

redis_client = redis.Redis(host='redis', port='6379')

CHARACTERS = string.ascii_letters + string.digits + '-_'


def get_random_string():
    return ''.join(random.choice(CHARACTERS) for _ in range(8))


def get_session_instance(request):
    if not request.session.session_key:
        request.session.save()
    return Session.objects.get(session_key=request.session.session_key)


def create_url_instance(request, data):
    url_subpart = data.get('url_subpart', '')
    while not url_subpart:
        url_subpart = get_random_string()
        if Url.objects.filter(url_subpart=url_subpart).count() > 0:
            url_subpart = ''
    url = Url.objects.create(
        original_url=data['original_url'],
        url_subpart=url_subpart,
        session=get_session_instance(request)
    )
    return url


def get_redirect_url(url_subpart):
    try:
        url = redis_client.get(url_subpart)
        if url:
            url = url.decode()
        else:
            url = get_object_or_404(Url, url_subpart=url_subpart)
            redis_client.set(url.url_subpart, url.original_url, ex=600)
            url = url.original_url
    except redis.exceptions.ConnectionError as error:
        logger.error(error)
        url = get_object_or_404(Url, url_subpart=url_subpart)
        url = url.original_url
    return url
