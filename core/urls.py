from django.urls import path

from core.views import HomePageView, RedirectUrlPage

app_name = 'core'

urlpatterns = [
    path('', HomePageView.as_view(), name='home-page'),
    path('r/<str:url_subpart>/', RedirectUrlPage.as_view(), name='redirect-page'),
]
