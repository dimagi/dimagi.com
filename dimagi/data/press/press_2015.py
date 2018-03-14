from datetime import date
from django.utils.translation import ugettext_lazy

from dimagi.pages.models.press import Press

PRESS = [
    Press(
        title=ugettext_lazy(
            "The Surprising Tech Saving Pregnant Women's Lives In "
            "Sub-Saharan Africa"
        ),
        source=ugettext_lazy(
            "Refinery29"
        ),
        url="http://www.refinery29.uk/2015/12/99098/pathfinder-international-"
            "mobile-phone-tech-africa-childbirth",
        date=date(2015, 12, 14),
    ),
    Press(
        title=ugettext_lazy(
            "Introduction of Mobile Health Tools to Support Ebola "
            "Surveillance and Contact Tracing in Guinea"
        ),
        source=ugettext_lazy(
            "Global Health: Science and Practice Journal"
        ),
        url="http://www.ghspjournal.org/content/3/4/646",
        date=date(2015, 12, 1),
    ),
    Press(
        title=ugettext_lazy(
            "Tableau Foundation: Building a Better World with Data"
        ),
        source=ugettext_lazy(
            "Flip the Media"
        ),
        url="http://flipthemedia.com/2015/11/tableau-foundation-"
            "building-better-world-data/",
        date=date(2015, 11, 20),
    ),
    Press(
        title=ugettext_lazy(
            "The 25 Best Large-Company Cultures in 2015"
        ),
        source=ugettext_lazy(
            "Entrepreneur"
        ),
        url="https://www.entrepreneur.com/article/252327",
        date=date(2015, 11, 4),
    ),
    Press(
        title=ugettext_lazy(
            "Using Data to Stay One Step Ahead of Ebola"
        ),
        source=ugettext_lazy(
            "Tableau Foundation"
        ),
        url="https://www.tableau.com/solutions/customer/using-data-stay-one-"
            "step-ahead-ebola",
        date=date(2015, 11, 1),
    ),
    Press(
        title=ugettext_lazy(
            "The Introduction of the Mobile Application 'CommCare' in Ebola "
            "Contact Tracing and Information Management Related to Patients"
        ),
        source=ugettext_lazy(
            "UNFPA"
        ),
        url="http://wcaro.unfpa.org/news/introduction-mobile-application-"
            "commcare-ebola-contact-tracing-and-information-management"
            "?page=2%2C12",
        date=date(2015, 10, 15),
    ),
    Press(
        title=ugettext_lazy(
            "3 mHealth projects you should know about"
        ),
        source=ugettext_lazy(
            "Devex"
        ),
        url="https://www.devex.com/news/3-mhealth-projects-you-should-know-"
            "about-87069",
        date=date(2015, 10, 9),
    ),
    Press(
        title=ugettext_lazy(
            "What Entrepreneur360 'Controllers' Know: Watch Markets and Keep "
            "the Customer Happy"
        ),
        source=ugettext_lazy(
            "Entrepreneur"
        ),
        url="https://www.entrepreneur.com/article/251283",
        date=date(2015, 10, 7),
    ),
    Press(
        title=ugettext_lazy(
            "10 private digital health companies reveal their 2014 revenue"
        ),
        source=ugettext_lazy(
            "MobileHealthNews"
        ),
        url="http://www.mobihealthnews.com/46204/10-private-digital-health-"
            "companies-reveal-their-2014-revenue",
        date=date(2015, 8, 19),
    ),
    Press(
        title=ugettext_lazy(
            "Open-source software boost for public health sector"
        ),
        source=ugettext_lazy(
            "Times of India"
        ),
        url="https://timesofindia.indiatimes.com/city/nagpur/Open-source-"
            "software-boost-for-public-health-sector/articleshow/48382959.cms",
        date=date(2015, 8, 7),
    ),
    Press(
        title=ugettext_lazy(
            "The Next Generation of Community Health Worker Programs"
        ),
        source=ugettext_lazy(
            "Huffington Post"
        ),
        url="https://www.huffingtonpost.com/john-m-zervos/the-next-"
            "generation-of-co_1_b_7152994.html",
        date=date(2015, 6, 27),
    ),
    Press(
        title=ugettext_lazy(
            "Top 20 Mobile Health (mHealth) Companies 2015 Innovators in "
            "Mobile Fitness, Telemedicine, eHealth & Remote Patient Monitoring"
        ),
        source=ugettext_lazy(
            "PR Newswire"
        ),
        url="https://www.prnewswire.com/news-releases/top-20-mobile-health-"
            "mhealth-companies-2015-innovators-in-mobile-fitness-"
            "telemedicine-ehealth--remote-patient-monitoring-502553951.html",
        date=date(2015, 5, 5),
    ),
    Press(
        title=ugettext_lazy(
            "Taking action in Africa"
        ),
        source=ugettext_lazy(
            "MIT News"
        ),
        url="http://news.mit.edu/2015/mit-sloan-africa-innovate-"
            "conference-0407",
        date=date(2015, 4, 7),
    ),
    Press(
        title=ugettext_lazy(
            "The Mobile Healthcare (mHealth) Bible: 2015 - 2020 - Analysis "
            "of the $13 Billion Market Featuring 750+ Vendors"
        ),
        source=ugettext_lazy(
            "PR Newswire"
        ),
        url="https://www.prnewswire.com/news-releases/the-mobile-healthcare-"
            "mhealth-bible-2015---2020---analysis-of-the-13-billion-market-"
            "featuring-750-vendors-300061917.html",
        date=date(2015, 4, 7),
    ),
    Press(
        title=ugettext_lazy(
            "Dimagi gets USAID funding to bring Ebola tracking apps to "
            "West Africa"
        ),
        source=ugettext_lazy(
            "Beta Boston"
        ),
        url="http://www.betaboston.com/news/2015/02/17/dimagi-gets-usaid-"
            "funding-to-bring-ebola-tracking-apps-to-west-africa/",
        date=date(2015, 2, 17),
    ),
    Press(
        title=ugettext_lazy(
            "Three NGOs Fighting Tuberculosis With Mobile Tech"
        ),
        source=ugettext_lazy(
            "Forbes"
        ),
        url="https://www.forbes.com/sites/techonomy/2015/01/13/three-ngos-"
            "fighting-tuberculosis-with-mobile-tech/#777c95f73de2",
        date=date(2015, 1, 13),
    ),
]
