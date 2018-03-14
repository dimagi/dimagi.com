from datetime import date
from django.utils.translation import ugettext_lazy

from dimagi.pages.models.press import Press

PRESS = [
    Press(
        title=ugettext_lazy(
            "Three Technologies that Could Transform Health Supply Chains"
        ),
        source=ugettext_lazy(
            "Chemonics"
        ),
        url="https://www.chemonics.com/three-technologies-that-could-"
            "transform-health-supply-chains/",
        date=date(2016, 11, 10),
    ),
    Press(
        title=ugettext_lazy(
            "Mount Sinai’s Research Arm Using Data Analytics to Address "
            "Health Inequities"
        ),
        source=ugettext_lazy(
            "Healthcare Informatics Institute"
        ),
        url="https://www.healthcare-informatics.com/news-item/analytics/mount-"
            "sinai-health-system-s-research-arm-using-data-analytics-address-"
            "health/",
        date=date(2016, 10, 25),
    ),
    Press(
        title=ugettext_lazy(
            "USAID Funds Partnership between Mount Sinai’s Arnhold Institute "
            "for Global Health and Dimagi to Identify and Forecast Zika Cold "
            "Spots Before They Become Hot Spots"
        ),
        source=ugettext_lazy(
            "Mount Sinai Press Release"
        ),
        url="https://www.mountsinai.org/about/newsroom/2016/usaid-funds-"
            "partnership-between-mount-sinais-arnhold-institute-for-global-"
            "health-and-dimagi-to-identify-and-forecast-zika-cold-spots-"
            "before-they-become-hot-spots",
        date=date(2016, 10, 17),
    ),
    Press(
        title=ugettext_lazy(
            "IBM Project DataWorks: Joining Multi-Sourced Data for AI-based "
            "Analytics"
        ),
        source=ugettext_lazy(
            "EnterpriseTech"
        ),
        url="https://www.enterprisetech.com/2016/09/27/ibm-project-dataworks-"
            "joining-multi-sourced-data-ai-based-analytics/",
        date=date(2016, 9, 26),
    ),
    Press(
        title=ugettext_lazy(
            "Why Sri Lanka needs to address the gender digital divide"
        ),
        source=ugettext_lazy(
            "DailyMirror"
        ),
        url="http://www.dailymirror.lk/114659/Why-Sri-Lanka-needs-to-address-"
            "the-gender-digital-divide",
        date=date(2016, 8, 25),
    ),
    Press(
        title=ugettext_lazy(
            "We know more about epidemics than ever before. Now what?"
        ),
        source=ugettext_lazy(
            "Devex"
        ),
        url="https://www.devex.com/news/we-know-more-about-epidemics-than-"
            "ever-before-now-what-88536",
        date=date(2016, 8, 8),
    ),
    Press(
        title=ugettext_lazy(
            "Ghanaian health workers use mobile phones to collect real-time "
            "maternal health data"
        ),
        source=ugettext_lazy(
            "World Health Organization"
        ),
        url="http://www.who.int/features/2016/Ghana-phone-maternal/en/",
        date=date(2016, 8, 1),
    ),
    Press(
        title=ugettext_lazy(
            "Data as a driver for change: How results can reshape work, "
            "but also deceive"
        ),
        source=ugettext_lazy(
            "Devex"
        ),
        url="https://www.devex.com/news/data-as-a-driver-for-change-how-"
            "results-can-reshape-work-but-also-deceive-88422",
        date=date(2016, 7, 18),
    ),
    Press(
        title=ugettext_lazy(
            "Simprints to launch mobile biometrics in Nepal"
        ),
        source=ugettext_lazy(
            "Business Weekly"
        ),
        url="https://www.businessweekly.co.uk/tech-trail/tech-profiles/"
            "simprints-launch-mobile-biometrics-nepal",
        date=date(2016, 6, 19),
    ),
    Press(
        title=ugettext_lazy(
            "Dimagi with Mohini Bhavsar"
        ),
        source=ugettext_lazy(
            "Aidpreneur"
        ),
        url="http://aidpreneur.com/tor-110-dimagi-with-mohini-bhavsar/",
        date=date(2016, 6, 7),
    ),
    Press(
        title=ugettext_lazy(
            "How mobile health technology aided Ebola response"
        ),
        source=ugettext_lazy(
            "TechTarget"
        ),
        url="http://searchmobilecomputing.techtarget.com/news/450297862/"
            "How-mobile-health-technology-aided-Ebola-response",
        date=date(2016, 6, 6),
    ),
    Press(
        title=ugettext_lazy(
            "CommCare: A custom mobile platform that is changing the face "
            "of Tostan's monitoring and evaluation"
        ),
        source=ugettext_lazy(
            "Tostan"
        ),
        url="https://www.tostan.org/commcare-custom-mobile-platform-"
            "changing-face-tostans-monitoring-and-evaluation/",
        date=date(2016, 5, 31),
    ),
    Press(
        title=ugettext_lazy(
            "Women’s Groups or Organizations Working on Gender-Based Violence "
            "Need Simple Yet efficient Tools to Measure Their Impact and "
            "Improve Their Processes"
        ),
        source=ugettext_lazy(
            "Womanity"
        ),
        url="https://womanity.org/how-simple-mobile-apps-can-help-womens-"
            "organizations-grow-their-impact/",
        date=date(2016, 4, 11),
    ),
    Press(
        title=ugettext_lazy(
            "What can technology do for global health?"
        ),
        source=ugettext_lazy(
            "World Economic Forum"
        ),
        url="https://www.weforum.org/agenda/2016/02/how-can-we-leverage-"
            "technology-to-bridge-the-global-healthcare-divide",
        date=date(2016, 2, 4),
    ),
    Press(
        title=ugettext_lazy(
            "Social Entrepreneurship: Connecting the "
            "Worlds of Education and Health Care"
        ),
        source=ugettext_lazy(
            "The74Million.org"
        ),
        url="https://www.the74million.org/article/social-entrepreneurship-"
            "connecting-the-worlds-of-education-and-health-care/",
        date=date(2016, 1, 25),
    ),
    Press(
        title=ugettext_lazy(
            "5 tips for social enterprises looking to scale"
        ),
        source=ugettext_lazy(
            "Devex"
        ),
        url="https://www.devex.com/news/5-tips-for-social-enterprises-"
            "looking-to-scale-87391",
        date=date(2016, 1, 11),
    ),
]
