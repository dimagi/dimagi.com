from __future__ import absolute_import

from django.utils.translation import ugettext_lazy
from dimagi.pages.models.sectors import Sector


SECTOR = Sector(
    name=ugettext_lazy(
        "Healthcare Delivery"
    ),
    summary=ugettext_lazy(
        "mHealth apps can help with women and child healthcare, nutrition programs, and disease treatment."
    ),
    template="data/sectors/content/child_health.html",
    icon="svg/sectors/healthcare/healthcare_delivery.html",
    theme="blue",
    slug="child-health",
)


SECTOR.add_sub_sectors([
    Sector(
        name=ugettext_lazy(
            "Maternal and Child Health"
        ),
        summary=ugettext_lazy(
        "Mobile tools help monitor and improve maternal, antenatal, natal, and postnatal care."
        ),
        template="data/sectors/content/child_health.html",
        icon="svg/sectors/healthcare/maternal_and_childhealth.html",
        theme="blue-theme",
        slug='sector_maternal_and_child_health',
        is_v2=True,
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
        "Support and track nutrition program performance with mobile data collection."
        ),
        template="data/sectors/content/child_health.html",
        icon="svg/sectors/healthcare/nutrition.html",
        theme="blue-theme",
        slug="sector_nutrition_programs",
        is_v2=True,
    ),
    Sector(
        name=ugettext_lazy(
            "Infectious Disease"
        ),
        summary=ugettext_lazy(
        "Treat widespread disease such as Tuberculosis, Ebola, and HIV/AIDS with mobile tools."
        ),
        template="data/sectors/content/child_health.html",
        icon="svg/sectors/healthcare/disease_treatment.html",
        theme="blue-theme",
        slug="sector_disease_treatment",
        is_v2=True,
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
        slug="sector_reproductive_health",
        is_v2=True,
    ),
    Sector(
        name=ugettext_lazy(
            "Vaccine Delivery"
        ),
        summary=ugettext_lazy(
        "Register, identify, and follow both vaccine recipients and clinic stock.."
        ),
        template="data/sectors/content/vaccine_delivery.html",
        icon="svg/sectors/healthcare/vaccine_delivery.html",
        theme="blue-theme",
        slug="sector_vaccine_delivery",
        is_v2=True,
    ),
])
