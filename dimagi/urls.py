from __future__ import absolute_import
from django.conf.urls import url, include
import dimagi.pages.views as pages
from dimagi.pages.views import commcare
from dimagi.pages.urls import blog
from dimagi.pages.urls import team
from dimagi.pages.views import redirect


urlpatterns = [
    url(r'^$', pages.home, name='home'),
    url(r'^services/$', pages.services, name='services'),
    url(r'^contact/$', pages.contact,  name='contact'),
    url(r'^certified-partners/$', commcare.partners, name='partner_program'),
    url(r'^blog/', include(blog.blog_urls)),
    url(r'^about/', include(team.about_urls)),
    url(r'^team/', include(team.team_urls)),

    url(r'^careers/', include('dimagi.pages.urls.careers')),
    url(r'^commcare/', include('dimagi.pages.urls.commcare')),
    url(r'^case-studies/', include('dimagi.pages.urls.case_studies')),
    url(r'^toolkits/', include('dimagi.pages.urls.toolkits')),
    url(r'^sectors/', include('dimagi.pages.urls.sectors')),
    url(r'^press/', include('dimagi.pages.urls.press')),
    url(r'^policy/', include('dimagi.pages.urls.policies')),


    # redirects - MUST be here for APPEND_SLASH to work
    url(r'^products$', redirect.page('commcare')),
    url(r'^products/$', redirect.page('commcare')),
    url(r'^partners/$', redirect.page('commcare')),
    url(r'^learn/$', redirect.page('contact')),
    url(r'^support/$', redirect.page('contact')),
    url(r'^content/smartcare.html$', redirect.page('blog_home')),

    url(r'^content/rapidandroid.html$',
        redirect.blog(
            'rapid-android-presented-at-unicefs-web4dev-conference')),
    url(r'^10-things-that-happened-in-2014-at-dimagi/$',
        redirect.blog('10-things-that-happened-in-2014-at-dimagi')),
    url(r'^bhoma/$',
        redirect.blog('bhoma-project-featured-on-couchone-com'),
        name="bhoma_redirect"),
    url(r'^dimagi-to-host-commcare-workshop-in-myanmar/$',
        redirect.blog('dimagi-to-host-commcare-workshop-in-myanmar')),
    url(r'^udt-how-quickly-do-frontline-workers-adopt-mobile-technology/$',
        redirect.blog('udt-how-quickly-do-frontline-workers-adopt-mobile-technology')),
    url(r'^introduction-under-the-data-tree-blog-series/$',
        redirect.blog('introduction-under-the-data-tree-blog-series')),
    url(r'^self-starter-blog-aquaya-on-implementing-commcare-for-water-projects-in-senegal/$',
        redirect.blog('self-starter-blog-aquaya-on-implementing-commcare-for-water-projects-in-senegal')),

]
