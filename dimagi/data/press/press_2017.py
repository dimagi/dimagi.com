from datetime import date
from django.utils.translation import ugettext_lazy

from dimagi.pages.models.press import Press

PRESS = [
    Press(
        title=ugettext_lazy(
            "Abt Associates to Tackle Vector-Borne Diseases Worldwide"
        ),
        source=ugettext_lazy(
            "PRWeb.com"
        ),
        url="http://www.prweb.com/releases/2017/10/prweb14779126.htm",
        date=date(2017, 10, 10),
    ),
    Press(
        title=ugettext_lazy(
            "Meet Jonathan Jackson of Dimagi in Cambridge"
        ),
        source=ugettext_lazy(
            "Boston Voyager"
        ),
        url="http://bostonvoyager.com/interview/"
            "meet-jonathan-jackson-dimagi-cambridge-ma/",
        date=date(2017, 9, 25),
    ),
    Press(
        title=ugettext_lazy(
            "Alum Helps Speed Healthcare to Remote Places"
        ),
        source=ugettext_lazy(
            "MIT Alumni"
        ),
        url="https://alum.mit.edu/slice/"
            "alum-helps-speed-healthcare-remote-places",
        date=date(2017, 6, 13),
    ),
    Press(
        title=ugettext_lazy(
            "Q&A: Jessica Hall on making the switch to digital data collection"
        ),
        source=ugettext_lazy(
            "Devex"
        ),
        url="https://www.devex.com/news/q-a-jessica-hall-on-making-the-"
            "switch-to-digital-data-collection-90457",
        date=date(2017, 6, 9),
    ),
    Press(
        title=ugettext_lazy(
            "5 Inventions Created To Prevent The Epidemic Of Maternal "
            "Mortality Around The World"
        ),
        source=ugettext_lazy(
            "GirlTalkHQ"
        ),
        url="http://girltalkhq.com/inventions-created-prevent-epidemic-"
            "maternal-mortality-around-world/",
        date=date(2017, 6, 2),
    ),
    Press(
        title=ugettext_lazy(
            "Dimagi's mission to revolutionise the world's public health data"
        ),
        source=ugettext_lazy(
            "Business Call to Action"
        ),
        url="https://www.businesscalltoaction.org/news/dimagis-mission-"
            "revolutionise-worlds-public-health-data",
        date=date(2017, 4, 15),
    ),
    Press(
        title=ugettext_lazy(
            "Scaling Up Sustainable Agriculture Through Technology: "
            "The Rainforest Alliance Launches Farmer Training App"
        ),
        source=ugettext_lazy(
            "Rainforest Alliance"
        ),
        url="https://www.rainforest-alliance.org/press-releases/"
            "farmer-training-app-launch",
        date=date(2017, 4, 4),
    ),
    Press(
        title=ugettext_lazy(
            "Mobile Technology Allows Community Health Workers to Quickly "
            "Identify & Refer in Côte d’Ivoire"
        ),
        source=ugettext_lazy(
            "Huffington Post"
        ),
        url="https://www.huffingtonpost.com/entry/58d53858e4b0f633072b36d6",
        date=date(2017, 3, 24),
    ),
    Press(
        title=ugettext_lazy(
            "Announcing funding for 10 Development Data Innovation projects"
        ),
        source=ugettext_lazy(
            "The World Bank"
        ),
        url="https://blogs.worldbank.org/opendata/announcing-funding-10-"
            "development-data-innovation-projects",
        date=date(2017, 3, 7),
    ),
]
