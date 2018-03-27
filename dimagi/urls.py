from __future__ import absolute_import
from django.conf.urls import url, include
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView

import dimagi.pages.views as pages
from dimagi.data.case_studies.mhealth import supply_chain_tanzania
from dimagi.data.sectors.sector import (
    child_health,
    mlabor,
    education,
    hiv_aids,
)
from dimagi.pages.sitemaps import (
    BlogPostSitemap,
    MainViewSitemap,
    BlogArchiveCategorySitemap,
    SectorSitemap,
    CaseStudySitemap,
    ToolkitSitemap,
    JobsSitemap,
    TeamMemberSitemap,
)
from dimagi.pages.views import commcare
from dimagi.pages.urls import blog
from dimagi.pages.urls import team
from dimagi.pages.views import redirect


sitemaps = {
    'main': MainViewSitemap,
    'sector': SectorSitemap,
    'case_study': CaseStudySitemap,
    'toolkit': ToolkitSitemap,
    'jobs': JobsSitemap,
    'team_member': TeamMemberSitemap,
    'archive': BlogArchiveCategorySitemap,
    'blog': BlogPostSitemap,
}


urlpatterns = [
    url(r'^$', pages.home, name='home'),
    url(r'^services/$', pages.services, name='services'),
    url(r'^contact/$', pages.contact,  name='contact'),
    url(r'^test_500/$', pages.test_500),
    url(r'^test_404/$', pages.test_404),
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
    url(r'^products/$', redirect.page('commcare')),
    url(r'^partners/$', redirect.page('commcare')),
    url(r'^smartcare/$', redirect.page('commcare')),
    url(r'^open-data-kit/$', redirect.page('commcare')),
    url(r'^mobile-health/$', redirect.page('commcare')),
    url(r'^diabetnet/$', redirect.page('commcare')),
    url(r'^diabetnet.shtml$', redirect.page('commcare')),
    url(r'^content/smartcare.html$', redirect.page('commcare')),
    url(r'^content/rapidandroid.html$', redirect.page('commcare')),
    url(r'^content/javarosa.html$', redirect.page('commcare')),
    url(r'^content/hiv-confidant.html$', redirect.page('commcare')),
    url(r'^content/commcare.html$', redirect.page('commcare')),
    url(r'^confidant.shtml$', redirect.page('commcare')),
    url(r'^commtrack/$', redirect.page('commcare')),
    url(r'^collaborate/openrosa/$', redirect.page('commcare')),

    url(r'^learn/$', redirect.page('contact')),
    url(r'^support/$', redirect.page('contact')),
    url(r'^connect-with-us/$', redirect.page('contact')),
    url(r'^collaborate/contact-us/$', redirect.page('contact')),
    url(r'^collaborate/community-support/$', redirect.page('contact')),

    url(r'^commcare-bangladesh/$', redirect.page('blog_home')),
    url(r'^commcare-afghanistan/$', redirect.page('blog_home')),
    url(r'^collaborate/coded-in-country/$', redirect.page('blog_home')),
    url(r'^cervical-cancer-screening/$', redirect.page('blog_home')),
    url(r'^blackberry-dictations/$', redirect.page('blog_home')),
    url(r'^august-talks-roundup/$', redirect.page('blog_home')),
    url(r'^aremind/$', redirect.page('blog_home')),
    url(r'^announcing-dimagi-south-africas-commcare-training-centre/$', redirect.page('blog_home')),
    url(r'^an-explanation-of-recent-commcare-hq-issues/$', redirect.page('blog_home')),

    url(r'^category/blog/(?P<category>[\w-]+)/$', redirect.blog_old_category),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$', redirect.dimagispace),

    url(r'^training/$', redirect.page('home')),
    url(r'^tostan/$', redirect.page('home')),
    url(r'^technology-strategy/$', redirect.page('home')),
    url(r'^technologies/$', redirect.page('home')),
    url(r'^software-development/$', redirect.page('home')),
    url(r'^rapidandroid/$', redirect.page('home')),
    url(r'^index.shtml$', redirect.page('home')),
    url(r'^home.php$', redirect.page('home')),
    url(r'^sms/$', redirect.page('home')),
    url(r'^health/$', redirect.page('home')),
    url(r'^header-style-2-clean-top-bar/$', redirect.page('home')),
    url(r'^shared-records/$', redirect.page('home')),
    url(r'^content/$', redirect.page('home')),
    url(r'^carehq/$', redirect.page('home')),
    url(r'^afrisis/$', redirect.page('home')),

    url(r'^technical-project-manager-2/$', redirect.page('careers')),
    url(r'^senior-software-engineer/$', redirect.page('careers')),
    url(r'^qa-and-support-analyst/$', redirect.page('careers')),

    url(r'^team.html$', redirect.page('team')),
    url(r'^about-mgmt.php$', redirect.page('about')),

    url(r'^mobile-e-imci/$', redirect.sector(child_health.SECTOR.slug)),
    url(r'^content/mobile-e-imci.html$', redirect.sector(child_health.SECTOR.slug)),
    url(r'^mlabour/$', redirect.sector(mlabor.SECTOR.slug)),
    url(r'^ivr-mobile-education/$', redirect.sector(education.SECTOR.slug)),
    url(r'^education/$', redirect.sector(education.SECTOR.slug)),
    url(r'^hiv-support/$', redirect.sector(hiv_aids.SECTOR.slug)),

    url(r'^commcare-tanzania/$', redirect.case_study(supply_chain_tanzania.STUDY.slug)),

    # Externally Linked Blog Post Redirects
    url(r'^content/rapidandroid.html$', redirect.blog('rapid-android-presented-at-unicefs-web4dev-conference')),
    url(r'^10-things-that-happened-in-2014-at-dimagi/$', redirect.blog('10-things-that-happened-in-2014-at-dimagi')),
    url(r'^bhoma/$', redirect.blog('bhoma-project-featured-on-couchone-com')),
    url(r'^udt-how-quickly-do-frontline-workers-adopt-mobile-technology/$', redirect.blog('udt-how-quickly-do-frontline-workers-adopt-mobile-technology')),
    url(r'^self-starter-blog-aquaya-on-implementing-commcare-for-water-projects-in-senegal/$', redirect.blog('self-starter-blog-aquaya-on-implementing-commcare-for-water-projects-in-senegal')),
    url(r'^world-aids-day-in-dodoma/$', redirect.blog('world-aids-day-in-dodoma')),
    url(r'^whats-it-like-training-300-chws-to-use-commcare-in-haiti/$', redirect.blog('whats-it-like-training-300-chws-to-use-commcare-in-haiti')),
    url(r'^what-did-i-learn-in-15-months-at-dimagi/$', redirect.blog('what-did-i-learn-in-15-months-at-dimagi')),
    url(r'^webinars-de-commcare-en-espanol/$', redirect.blog('webinars-de-commcare-en-espanol')),
    url(r'^using-commcare-for-cmam/$', redirect.blog('using-commcare-for-cmam')),
    url(r'^usaid-nominates-dimagi-for-the-fighting-ebola-grand-challenge-award/$', redirect.blog('usaid-nominates-dimagi-for-the-fighting-ebola-grand-challenge-award')),
    url(r'^usaid-mhealth-compendium-vol-4/$', redirect.blog('usaid-mhealth-compendium-vol-4')),
    url(r'^usaid-awards-dimagi-partners-500000-to-expand-domestic-violence-reporting/$', redirect.blog('usaid-awards-dimagi-partners-500000-to-expand-domestic-violence-reporting')),
    url(r'^unfpa-writes-about-dimagis-anti-ebola-work/$', redirect.blog('unfpa-writes-about-dimagis-anti-ebola-work')),
    url(r'^udt-is-it-unusual-for-a-users-activity-level-to-change-quickly/$', redirect.blog('udt-is-it-unusual-for-a-users-activity-level-to-change-quickly')),
    url(r'^udt-does-technology-matter-in-commcare-projects/$', redirect.blog('udt-does-technology-matter-in-commcare-projects')),
    url(r'^three-ways-to-achieve-economies-of-scale-in-mhealth/$', redirect.blog('three-ways-to-achieve-economies-of-scale-in-mhealth')),
    url(r'^take-a-tablet-a-blog-by-colalife/$', redirect.blog('take-a-tablet-a-blog-by-colalife')),
    url(r'^social-good-webinar-with-dimagi-ceo/$', redirect.blog('social-good-webinar-with-dimagi-ceo')),
    url(r'^saijai-liangpunsakul-awarded-for-mhealth-work/$', redirect.blog('saijai-liangpunsakul-awarded-for-mhealth-work')),
    url(r'^recognizing-international-womens-day/$', redirect.blog('recognizing-international-womens-day')),
    url(r'^recap-dimagi-hosts-its-first-tech-summit/$', redirect.blog('recap-dimagi-hosts-its-first-tech-summit')),
    url(r'^pulling-data-from-couchdb-to-a-relational-database-made-easy-with-_changes/$', redirect.blog('pulling-data-from-couchdb-to-a-relational-database-made-easy-with-changes')),
    url(r'^new-feature-lookup-table-question-type/$', redirect.blog('new-feature-lookup-table-question-type')),
    url(r'^motech-suite-workshop-a-quick-recap/$', redirect.blog('motech-suite-workshop-a-quick-recap')),
    url(r'^motech-and-commcare-highlighted-in-huffington-post/$', redirect.blog('motech-and-commcare-highlighted-in-huffington-post')),
    url(r'^mobile-device-helps-nurses-identify-domestic-violence-in-bangalore-india/$', redirect.blog('mobile-device-helps-nurses-identify-domestic-violence-in-bangalore-india')),
    url(r'^mobile-applications-for-healthcare-workers/$', redirect.blog('mobile-applications-for-healthcare-workers')),
    url(r'^mobile-application-strengthens-myanmars-fight-against-mdr-tb/$', redirect.blog('mobile-application-strengthens-myanmars-fight-against-mdr-tb')),
    url(r'^life-in-the-clouds-boosting-haitian-health-care-through-technology/$', redirect.blog('life-in-the-clouds-boosting-haitian-health-care-through-technology')),
    url(r'^le-canada-finance-des-projets-de-deploiement-a-lechelle-de-la-sante-mobile-en-afrique-de-louest/$', redirect.blog('le-canada-finance-des-projets-de-deploiement-a-lechelle-de-la-sante-mobile-en-afrique-de-louest')),
    url(r'^issues-with-commcarehq-reports/$', redirect.blog('issues-with-commcarehq-reports')),
    url(r'^introduction-under-the-data-tree-blog-series/$', redirect.blog('introduction-under-the-data-tree-blog-series')),
    url(r'^how-commcare-is-improving-the-work-of-a-salesman-in-senegal/$', redirect.blog('how-commcare-is-improving-the-work-of-a-salesman-in-senegal')),
    url(r'^hitting_100/$', redirect.blog('hitting-100')),
    url(r'^hands-down-the-happiest-community-ive-ever-seen/$', redirect.blog('hands-down-the-happiest-community-ive-ever-seen')),
    url(r'^from-a-dimagi-intern/$', redirect.blog('from-a-dimagi-intern')),
    url(r'^francais-un-blog-de-self-starter-aquaya-la-collecte-de-donnees-de-leau-au-senegal-avec-commcare/$', redirect.blog('francais-un-blog-de-self-starter-aquaya-la-collecte-de-donnees-de-leau-au-senegal-avec-commcare')),
    url(r'^four-months-out-of-peace-corps-reflections-about-mhealth/$', redirect.blog('four-months-out-of-peace-corps-reflections-about-mhealth')),
    url(r'^for-third-year-in-a-row-dimagi-makes-inc-5000-list/$', redirect.blog('for-third-year-in-a-row-dimagi-makes-inc-5000-list')),
    url(r'^fighting-malaria-with-a-cell-phone-theres-an-app-for-that/$', redirect.blog('fighting-malaria-with-a-cell-phone-theres-an-app-for-that')),
    url(r'^django-orm-memory-leaks-in-debug-mode-73877/$', redirect.blog('django-orm-memory-leaks-in-debug-mode-73877')),
    url(r'^dirty-guinea-pigs-and-spiders-brains-teaching-computers-in-rural-africa/$', redirect.blog('dirty-guinea-pigs-and-spiders-brains-teaching-computers-in-rural-africa')),
    url(r'^dirty-guinea-pigs-and-spiders-brains-teaching-computers-in-rural-africa/training_kafue_ts-jpg-scaled-1000/$', redirect.blog('dirty-guinea-pigs-and-spiders-brains-teaching-computers-in-rural-africa')),
    url(r'^dimagis-work-in-southeast-asia-highlighted-by-forbes/$', redirect.blog('dimagis-work-in-southeast-asia-highlighted-by-forbes')),
    url(r'^dimagis-may-conference-line-up/$', redirect.blog('dimagis-may-conference-line-up')),
    url(r'^dimagis-ebola-work-highlighted-in-politico-seattle-times/$', redirect.blog('dimagis-ebola-work-highlighted-in-politico-seattle-times')),
    url(r'^dimagis-cso-speaks-at-me-tech-conference/$', redirect.blog('dimagis-cso-speaks-at-me-tech-conference')),
    url(r'^dimagineering-what-stops-us-from-working/$', redirect.blog('dimagineering-what-stops-us-from-working')),
    url(r'^dimagi-to-host-workshop-on-mobile-apps-for-womens-empowerment-and-safety-in-new-delhi/$', redirect.blog('dimagi-to-host-workshop-on-mobile-apps-for-womens-empowerment-and-safety-in-new-delhi')),
    url(r'^dimagi-to-host-commcare-workshop-in-myanmar/$', redirect.blog('dimagi-to-host-commcare-workshop-in-myanmar')),
    url(r'^dimagi-to-give-a-nethope-webinar-about-commtrack/$', redirect.blog('dimagi-to-give-a-nethope-webinar-about-commtrack')),
    url(r'^dimagi-talks-about-responsible-innovation-and-social-entrepreneurship/$', redirect.blog('dimagi-talks-about-responsible-innovation-and-social-entrepreneurship')),
    url(r'^dimagi-seeking-usaid-research-fellows-for-senegal-india/$', redirect.blog('dimagi-seeking-usaid-research-fellows-for-senegal-india')),
    url(r'^dimagi-presents-at-unicef-haiti-event/$', redirect.blog('dimagi-presents-at-unicef-haiti-event')),
    url(r'^dimagi-presenting-at-mhealth-summits-global-mhealth-forum/$', redirect.blog('dimagi-presenting-at-mhealth-summits-global-mhealth-forum')),
    url(r'^dimagi-organise-un-webinaire-de-revue-generale-de-commcare/$', redirect.blog('dimagi-organise-un-webinaire-de-revue-generale-de-commcare')),
    url(r'^dimagi-mobileoct-awarded-funding-to-improve-cervical-cancer-screening/$', redirect.blog('dimagi-mobileoct-awarded-funding-to-improve-cervical-cancer-screening')),
    url(r'^dimagi-launches-commcare-exchange/$', redirect.blog('dimagi-launches-commcare-exchange')),
    url(r'^dimagi-joins-the-greentree-consensus/$', redirect.blog('dimagi-joins-the-greentree-consensus')),
    url(r'^dimagi-joins-efforts-to-respond-to-ebola-crisis-in-west-africa/$', redirect.blog('dimagi-joins-efforts-to-respond-to-ebola-crisis-in-west-africa')),
    url(r'^dimagi-is-on-the-road/$', redirect.blog('dimagi-is-on-the-road')),
    url(r'^dimagi-in-myanmar/$', redirect.blog('dimagi-in-myanmar')),
    url(r'^dimagi-in-brazil-or-why-you-should-stop-worrying-and-learn-to-love-making-your-employees-lives-awesome/$', redirect.blog('dimagi-in-brazil-or-why-you-should-stop-worrying-and-learn-to-love-making-your-employees-lives-awesome')),
    url(r'^dimagi-holding-first-technical-webinar/$', redirect.blog('dimagi-holding-first-technical-webinar')),
    url(r'^dimagi-gets-schooled-with-first-education-roundtable/$', redirect.blog('dimagi-gets-schooled-with-first-education-roundtable')),
    url(r'^dimagi-fellow-featured-from-india/$', redirect.blog('dimagi-fellow-featured-from-india')),
    url(r'^dimagi-coo-presents-on-cutting-edge-health-technology/$', redirect.blog('dimagi-coo-presents-on-cutting-edge-health-technology')),
    url(r'^dimagi-away-month-guatemala/$', redirect.blog('dimagi-away-month-guatemala')),
    url(r'^dimagi-awarded-development-innovation-venture-grant-from-usaid/$', redirect.blog('dimagi-awarded-development-innovation-venture-grant-from-usaid')),
    url(r'^dimagi-and-sydney-school-of-public-health-to-host-a-commcare-workshop/$', redirect.blog('dimagi-and-sydney-school-of-public-health-to-host-a-commcare-workshop')),
    url(r'^crs-remind-project-recognized-at-14th-world-congress-on-public-health/$', redirect.blog('crs-remind-project-recognized-at-14th-world-congress-on-public-health')),
    url(r'^continuing-commcare-in-togo/$', redirect.blog('continuing-commcare-in-togo')),
    url(r'^commcare-wins-vodafone-india-foundation-usaid-awards-in-southeast-asia/$', redirect.blog('commcare-wins-vodafone-india-foundation-usaid-awards-in-southeast-asia')),
    url(r'^commcare-papers-in-2014/$', redirect.blog('commcare-papers-in-2014')),
    url(r'^commcare-october-update-commcare-mobile-2-15-commcarehq-improvements/$', redirect.blog('commcare-october-update-commcare-mobile-2-15-commcarehq-improvements')),
    url(r'^commcare-dresses-and-deploying-mhealth-in-senegal/$', redirect.blog('commcare-dresses-and-deploying-mhealth-in-senegal')),
    url(r'^commcare-december-update-commcare-mobile-2-17-commcarehq-improvements/$', redirect.blog('commcare-december-update-commcare-mobile-2-17-commcarehq-improvements')),
    url(r'^commcare-august-update-commcare-mobile-2-14-commcarehq-improvements/$', redirect.blog('commcare-august-update-commcare-mobile-2-14-commcarehq-improvements')),
    url(r'^commcare-advanced-topics-workshop-in-malawi/$', redirect.blog('commcare-advanced-topics-workshop-in-malawi')),
    url(r'^care-coordination/$', redirect.blog('dimagi-awarded-phase-ii-sbir-for-cancer-coordination')),
    url(r'^canada-funds-mhealth-scale-up-projects-in-west-africa/$', redirect.blog('canada-funds-mhealth-scale-up-projects-in-west-africa')),
    url(r'^bhoma-project-featured-on-couchone-com/$', redirect.blog('bhoma-project-featured-on-couchone-com')),
    url(r'^announcing-two-commcare-webinars-in-march/$', redirect.blog('announcing-two-commcare-webinars-in-march')),
    url(r'^announcing-our-first-cape-town-user-group-meet-up/$', redirect.blog('announcing-our-first-cape-town-user-group-meet-up')),
    url(r'^announcing-guatemala-commcare-workshop-taller-de-commcare-para-principiantes-en-guatemala/$', redirect.blog('announcing-guatemala-commcare-workshop-taller-de-commcare-para-principiantes-en-guatemala')),
    url(r'^announcing-dimagis-first-boston-commcare-user-group-meeting/$', redirect.blog('announcing-dimagis-first-boston-commcare-user-group-meeting')),
    url(r'^announcing-commcare-webinars-in-april/$', redirect.blog('announcing-commcare-webinars-in-april')),
    url(r'^an-asha-calls-me-and-tells-me-stories-of-change/$', redirect.blog('an-asha-calls-me-and-tells-me-stories-of-change')),
    url(r'^africare-dimagi-project-selected-as-a-slb-finalist/$', redirect.blog('africare-dimagi-project-selected-as-a-slb-finalist')),
    url(r'^5-div-grantees-to-be-showcased-at-the-unga-mdg-countdown/$', redirect.blog('5-div-grantees-to-be-showcased-at-the-unga-mdg-countdown')),

    url(r'^google9633af922b8b0064.html$', pages.verify),
    url(r'^sitemap.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    url(r'^robots.txt$', TemplateView.as_view(template_name='robots.txt')),
]
