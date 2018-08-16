from django.shortcuts import render
from Drama.teleplay import teleplay
# from Drama.dispatch import dispatch
# from Drama.alarm import alarm
# from Drama.config import config

class Drama(object):

    def __init__(self, name='drama'):
        self._registry = {}  # model_class class -> admin_class instance
        self.name = name

    def get_urls(self):
        from django.conf.urls import url, include

        urlpatterns = [
            url(r'^teleplay/', include(teleplay.urls), name="teleplay"),
            # url(r'^dispatch/', include(dispatch.urls), name='dispatch'),
            # url(r'^alarm/', include(alarm.urls), name='alarm'),
            # url(r'^config/', include(config.urls), name='config'),


        ]
        return urlpatterns

    @property
    def urls(self):
        return self.get_urls(), 'drama', self.name

drama = Drama()
