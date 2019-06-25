from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.sectors import Sector, Project
from dimagi.data.sectors import  countries
from dimagi.data.case_studies import mhealth


SECTOR = Sector(
    name=ugettext_lazy(
        "Health Care Delivery"
    ),
    summary=ugettext_lazy(
        "mHealth apps can help with women and child healthcare, nutrition programs, and disease treatment."
    ),
    template="data/sectors/content/child_health.html",
    icon="svg/sectors/healthcare/healthcare_delivery.html",
    theme="blue-theme",
    slug="child-health",
)


SECTOR.add_sub_sectors([
    Sector(
        name=ugettext_lazy(
            "Maternal and Child Health"
        ),
        summary=ugettext_lazy(
        "Mobile tools can monitor and improve maternal, antenatal, natal, and postnatal care."
        ),
        template="data/sectors/content/child_health.html",
        icon="svg/sectors/healthcare/maternal_and_childhealth.html",
        theme="blue-theme",
        slug="child-health",
        slides=[
            "data/sectors/content/child_health/programs.html",
            "data/sectors/content/child_health/clinics.html",
            "data/sectors/content/child_health/patients.html",
        ],
        download_url="https://cdn2.hubspot.net/hubfs/503070/Child%20Health.pdf",
    ),
    Sector(
        name=ugettext_lazy(
            "Nutrition"
        ),
        summary=ugettext_lazy(
        "Support and track nutrition program performance with mobile data collection.."
        ),
        template="data/sectors/content/child_health.html",
        icon="svg/sectors/healthcare/nutrition.html",
        theme="blue-theme",
        slug="nutrition",
    ),
    Sector(
        name=ugettext_lazy(
            "Disease Treatment"
        ),
        summary=ugettext_lazy(
        "Treat widespread disease such as TB, Ebola, and HIV/AIDS with mobile tools."
        ),
        template="data/sectors/content/child_health.html",
        icon="svg/sectors/healthcare/disease_treatment.html",
        theme="blue-theme",
        slug="child-health",
    ),
    Sector(
        name=ugettext_lazy(
            "Reproductive Health"
        ),
        summary=ugettext_lazy(
        "Increase access to reproductive healthcare for women with mobile data collection."
        ),
        template="data/sectors/content/child_health.html",
        icon="svg/sectors/healthcare/reproductive_health.html",
        theme="blue-theme",
        slug="reproductive-health",
    ),
])
