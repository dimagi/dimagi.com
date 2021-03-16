from django.conf.urls import url


from dimagi.pages.views.sectors import (
    view_all,
    view_single,
    agriculture_extension_programs,
    agricultural_logistics,
    agricultural_cooperatives,
    agriculture_finance,
    sector_reproductive_health,
    sector_vaccine_delivery,
    nutrition_programs,
    maternal_and_child_health,
    disease_treatment,
    education,
    small_businesses,
    programmatic_research,
    financial_inclusion,
    gb_violence,
)


urlpatterns = [
    url(r'^$', view_all,
        name='sectors'),
    url(r'^agricultural-extension-programs/$', agriculture_extension_programs,
        name='sector_agriculture_extension_programs'),
    url(r'^agricultural-logistics/$', agricultural_logistics,
        name='agricultural_logistics'),
    url(r'^agricultural-cooperatives/$', agricultural_cooperatives,
        name='agricultural_cooperatives'),
    url(r'^agricultural-finance/$', agriculture_finance,
        name='sector_agricultural_finance'),
    url(r'^education/$', education,
        name='education'),
    url(r'^reproductive-health/$', sector_reproductive_health,
        name='sector_reproductive_health'),
    url(r'^vaccine-delivery/$', sector_vaccine_delivery,
        name='sector_vaccine_delivery'),
    url(r'^nutrition/$', nutrition_programs,
        name='sector_nutrition_programs'),
    url(r'^maternal-and-child-health/$', maternal_and_child_health,
        name='sector_maternal_and_child_health'),
    url(r'^programmatic-research/$', programmatic_research,
        name='programmatic_research'),
    url(r'^financial-inclusion/$', financial_inclusion,
        name='financial_inclusion'),
    url(r'^infectious-disease/$', disease_treatment,
        name='sector_disease_treatment'),
    url(r'^small-businesses/$', small_businesses,
        name='sector_small_businesses'),
    url(r'^gender-based-violence/$', gb_violence,
        name='gb_violence'),
    url(r'^(?P<slug>[\w-]+)/$', view_single,
        name='sector'),
]
