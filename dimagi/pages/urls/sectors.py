from django.conf.urls import url


from dimagi.pages.views.sectors import (
    view_all,
    view_single,
    agriculture_extension_programs,
    sector_reproductive_health,
    nutrition_programs,
    maternal_and_child_health,
    disease_treatment,
    education,
    small_businesses,
    programmatic_research,
)


urlpatterns = [
    url(r'^$', view_all,
        name='sectors'),
    url(r'^agricultural-extension-programs/$', agriculture_extension_programs,
        name='sector_agriculture_extension_programs'),
    url(r'^education/$', education,
        name='education'),
    url(r'^reproductive-health/$', sector_reproductive_health,
        name='sector_reproductive_health'),
    url(r'^nutrition/$', nutrition_programs,
        name='sector_nutrition_programs'),
    url(r'^maternal-and-child-health/$', maternal_and_child_health,
        name='sector_maternal_and_child_health'),
    url(r'^programmatic-research/$', programmatic_research,
        name='programmatic_research'),
    url(r'^disease-treatment/$', disease_treatment,
        name='sector_disease_treatment'),
    url(r'^small-businesses/$', small_businesses,
        name='sector_small_businesses'),
    url(r'^(?P<slug>[\w-]+)/$', view_single,
        name='sector'),
]
