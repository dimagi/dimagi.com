from django.conf.urls import url
import dimagi.pages.views


urlpatterns = [
    url(r'^$', dimagi.pages.views.home, name='page_home'),
]
