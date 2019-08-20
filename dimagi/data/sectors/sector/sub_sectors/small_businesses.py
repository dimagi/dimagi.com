from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.sectors import Sector, Project
from dimagi.data.sectors import countries


SECTOR = Sector(
    name=ugettext_lazy(
        "Small Businesses"
    ),
    summary=ugettext_lazy(
        "CommCare helps small businesses improve decision making."
    ),
    template="data/sectors/content/small_businesses.html",
    slug="small-businesses",
    theme="purple-theme",
    slides=[
        "data/sectors/content/small_businesses/small_businesses.html",
        "data/sectors/content/small_businesses/vendors.html",
        "data/sectors/content/small_businesses/customers.html",
    ],
    download_url="https://cdn2.hubspot.net/hubfs/503070/Small%20Business.pdf",
    hubspot_form="b0e76822-a232-4eb9-ac59-5554c10f4348",
    thumbnail = "pages/sectors/small-businesses/hero.jpg",
)

SECTOR.add_projects([
    Project(
        name=ugettext_lazy(
            "Pollinate Energy"
        ),
        country=countries.INDIA,
        description=ugettext_lazy("""
Pollinate Energy is an Indian-based NGO whose mission is to eradicate energy 
poverty through clean energy solutions, including solar-powered lights. 
Pollinate Energy’s CommCare application is used by the NGO’s “pollinators” 
to manage their energy solutions stock, complete community profile surveys,
and ensure that communities provide accurate and timely repayments for 
solar-powered lights. In addition to supporting Pollinators, the 
application also provides a solar-powered light installation guide for 
beneficiaries [Article].
        """),
    ),
    Project(
        name=ugettext_lazy(
            "Small Enterprise Foundation"
        ),
        country=countries.SOUTH_AFRICA,
        description=ugettext_lazy("""
Small Enterprise Foundation (SEF) is a non-profit, pro-poor microfinance 
institution working towards the alleviation and eventual eradication of 
poverty. SEF targets female-led small and medium enterprises with credit 
and savings services to foster sustainable income generation, 
job creation, and social empowerment throughout South Africa. 
The CommCare application helps SEF to ensure that all activities 
are performed according to internal policies and procedures; corrupt 
and/or fraudulent activities are prevented, identified and reported on; 
special assignments requested by senior managers are executed; weaknesses 
and/or threats to SEF are identified and preventative measures are 
recommended; and ensure the overall service to clients is of the highest quality.
        """),
    ),
    Project(
        name=ugettext_lazy(
            "Wits Health Consortium/The IMAGE Project"
        ),
        country=countries.SOUTH_AFRICA,
        description=ugettext_lazy("""
The Intervention with Microfinance for AIDS & Gender Equity (IMAGE Project), 
an NGO linked to the University of the Witwatersrand School of Public Health, 
combines a microfinance intervention with a gender/HIV awareness curriculum 
with the aim of improving the social and economic well being of households 
and reducing the risk of HIV infection and gender-based violence. The IMAGE
Project is currently working with 5000 households in 300 rural villages 
across four South African provinces – Limpopo, Gauteng, Northwest and 
KwaZulu Natal, with 35 field staff working in small, dispersed teams. 
The IMAGE Project uses CommCare to track the progress of individual loan 
clients with respect to economic well being, assess performance in the 
microfinance intervention, and collect periodic data on health and social 
outcomes. The IMAGE project also uses CommCare to conduct routine 
performance monitoring for program staff to assess the quality intervention 
delivery and the support and supervision received. The CommCare platform is 
digitizing paper-based routine assessment forms to achieve transparent, 
bi-directional and regular feedback.
    """),
    ),
    Project(
        name=ugettext_lazy(
            "UN WFP Cash Transfer"
        ),
        country=countries.ZAMBIA,
        description=ugettext_lazy("""
The Government of the Republic of Zambia (GRZ), with support from DFID, 
UNICEF and Irish Aid, is currently implementing social cash transfers 
(SCTs) in 13 districts with the objective of reducing extreme poverty 
and vulnerability. The program is transitioning from a paper-based 
system used since 2004 to CommCare, with the aim of addressing problems 
of data accuracy and completeness during registration and follow-up 
activities. Enumerators, CWAC leads, and District officers are equipped 
with a CommCare application to manage the enrollment, support, and 
tracking of all beneficiaries in the system. Case management enables 
field staff to review and update details to existing beneficiary data 
within the mobile application. Follow-up visit forms take into account 
beneficiary details and are customized according to the history of a 
given case. SMS reminders enable communication with beneficiaries and 
field staff without direct access to the application. Reminders are 
automated based on the information stored in each beneficiary’s case 
record. This solution goes beyond accurate data collection and closes 
the loop in the approval, payment distribution and follow-up processes.
    """),
    ),
    Project(
        name=ugettext_lazy(
            "Technoserve Tutawa Entrepreneur"
        ),
        country=countries.SOUTH_AFRICA,
        description=ugettext_lazy("""
TechnoServe is partnering with a national South African bank to provide business 
development services to beneficiaries of a regional business-grouping scheme. 
Technoserve business advisors provide tailored support to entrepreneurs by 
providing business development services that drive the competitiveness and 
sustainability of beneficiary businesses. The business advisors run CommCare 
on both tablets and laptop computers to improve timeliness of beneficiary visits 
and quality of services delivered. The application enables tracking of financial 
health of the beneficiaries as well as tracking services delivered to 
beneficiaries over time.
    """),
    ),
    Project(
        name=ugettext_lazy(
            "HOPE Mobile Money System"
        ),
        country=countries.INDIA,
        description=ugettext_lazy("""
HOPE is a system to pay existing incentives directly to mothers/ASHAs in their 
bank accounts. HOPE currently allows computer-based input of events for mothers. 
These are approved by the block accountant, which triggers payment to the bank 
account. An API has been developed to integrate data captured through another 
CommCare app with HOPE. The API exposes a list of all mothers and the “HOPE” 
events that have occurred for those mothers, which will eventually lead to 
payment. The API matches mothers with those in HOPE using the bank account number.
    """),
    ),
])
