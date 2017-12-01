from django.conf.urls import url
import dimagi.pages.views as pages


urlpatterns = [
    url(r'^$', pages.home, name='page_home'),
]
