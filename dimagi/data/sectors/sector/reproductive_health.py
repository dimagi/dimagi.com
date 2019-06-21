from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.sectors import Sector, Project
from dimagi.data.sectors import countries


SECTOR = Sector(
    name=ugettext_lazy(
        "Reproductive Health"
    ),
    summary=ugettext_lazy(
        "Increase access to reproductive health care for women using CommCare."
    ),
    template="data/sectors/content/reproductive_health.html",
    slug="reproductive-health",
    slides=[
        "data/sectors/content/reproductive_health/reproductive_health_programs.html",
        "data/sectors/content/reproductive_health/health_workers.html",
        "data/sectors/content/reproductive_health/health_facilities.html",
        "data/sectors/content/reproductive_health/patients.html",
    ],
    download_url="https://cdn2.hubspot.net/hubfs/503070/Reproductive%20Health.pdf",
)


SECTOR.add_projects([
    Project(
        name=ugettext_lazy(
            "D-Tree Family Planning Application"
        ),
        country=countries.TANZANIA,
        description=ugettext_lazy("""
D-Tree International and Dimagi have developed a CommCare application 
that monitors geographical demand for specific kinds of family planning 
methods. CHWs collect information on which method of contraception a 
woman is using versus which method she would have chosen had it been 
available. This data can inform programs on which forms of 
contraception are preferred.
        """),
    ),
    Project(
        name=ugettext_lazy(
            "IntraHealth Informed Push Model for Family Planning"
        ),
        country=countries.SENEGAL,
        description=ugettext_lazy("""
IntraHealth and Dimagi have worked together to develop and deploy 
a CommCare Supply application for the management of all family 
planning commodities in 1,400 facilities across Senegal. In this 
deployment, mobile logisticians equipped with commodities travel 
to each facility to perform inventory management tasks, track 
indicators, calculate resupply levels, and deliver commodities 
on the spot. Each logistician is equipped with a tablet running 
CommCare Supply which allows them to easily record, manage, and 
review stock information for hundreds of facilities. This 
intervention is currently being scaled nationally in Senegal.
        """),
    ),
    Project(
        name=ugettext_lazy(
            "International Federation of Gynecology and Obstetrics"
            " (FIGO) & Harvard School of Public Health – Sri Lanka,"
            " Nepal, Tanzania, Bangladesh, India, Kenya"
        ),
        country=countries.GLOBE,
        description=ugettext_lazy("""
The postpartum IUD initiative aims to address the postpartum contraceptive 
needs of women by training community midwives, health workers, doctors 
and delivery unit staff in postpartum IUD counseling and insertion. As 
part of this project, project staff are using CommCare to collect 
baseline and intervention data, including data with women at the 
hospital after delivery, at nine months, and at 18 months after delivery.
    """),
    ),

    Project(
        name=ugettext_lazy(
            "University Research Coalition ANCRE, Benin"
        ),
        country=countries.BENIN,
        description=ugettext_lazy("""
URC and Dimagi have launched a CommCare and CommCare Supply application 
that will equip 300 CHWs in 10 health zones of Benin to promote family 
planning methods, alerting them of stock outs, providing checklists and 
decision making support. The project also focuses heavily on supportive 
supervision, monitoring the frequency and duration of CHW visits to 
clients and behavior change counseling using multimedia.
    """),
    ),
])
