from datetime import date
from django.utils.translation import ugettext_lazy

from dimagi.pages.models.press import Press

PRESS = [
    Press(
        title=ugettext_lazy(
            "11 Amazing Apps That Are Using Mobile Phone For Social Good"
        ),
        source=ugettext_lazy(
            "The Better India"
        ),
        url="https://www.thebetterindia.com/16765/11-amazing-mobile-apps-"
            "transforming-way-rural-india-works-mobile4good14/",
        date=date(2014, 12, 4),
    ),
    Press(
        title=ugettext_lazy(
            "Are smartphones the right gift for West Africa's Ebola fight?"
        ),
        source=ugettext_lazy(
            "Politico"
        ),
        url="https://www.politico.com/story/2014/12/smartphones-ebola-113284",
        date=date(2014, 12, 2),
    ),
    Press(
        title=ugettext_lazy(
            "Tableau starts charity with pre-IPO shares"
        ),
        source=ugettext_lazy(
            "The Seattle Times"
        ),
        url="http://blogs.seattletimes.com/brierdudley/2014/12/01/tableau-"
            "starts-charity-with-pre-ipo-shares/",
        date=date(2014, 12, 1),
    ),
    Press(
        title=ugettext_lazy(
            "Southeast Asia's Health App Explosion"
        ),
        source=ugettext_lazy(
            "Forbes"
        ),
        url="https://www.forbes.com/sites/techonomy/2014/10/15/southeast-"
            "asias-health-app-explosion/#b38623423066",
        date=date(2014, 10, 15),
    ),
    Press(
        title=ugettext_lazy(
            "Southeast Asia has an acute healthcare problem. These apps "
            "inject hope"
        ),
        source=ugettext_lazy(
            "Tech in Asia"
        ),
        url="https://www.techinasia.com/apps-healthcare-problem-southeast-"
            "asia",
        date=date(2014, 10, 14),
    ),
    Press(
        title=ugettext_lazy(
            "For Africare, Saving Lives at Birth Means Bringing Innovation "
            "and Community Partnerships to Zambia and Senegal"
        ),
        source=ugettext_lazy(
            "Africare"
        ),
        url="https://www.africare.org/for-africare-saving-lives-at-birth-"
            "means-bringing-innovation-and-community-partnerships-to-zambia-"
            "and-senegal/",
        date=date(2014, 7, 17),
    ),
    Press(
        title=ugettext_lazy(
            "How technology and empathy can change lives: Saijai "
            "Liangpunsakul at TEDxAmRing"
        ),
        source=ugettext_lazy(
            "TEDx"
        ),
        url="https://www.youtube.com/watch?v=pVF1hUTVZ0w",
        date=date(2014, 6, 5),
    ),
    Press(
        title=ugettext_lazy(
            "Pathfinder to Launch CommCare as part of Groundbreaking mHealth "
            "Initiative in Haiti"
        ),
        source=ugettext_lazy(
            "Pathfinder"
        ),
        url="http://www.pathfinder.org/articles/pathfinder-launch-commcare-"
            "part-groundbreaking-mhealth-initiative-haiti/",
        date=date(2014, 4, 27),
    ),
    Press(
        title=ugettext_lazy(
            "Tackling Indian maternal deaths by smartphone"
        ),
        source=ugettext_lazy(
            "The Christian Science Monitor"
        ),
        url="https://www.csmonitor.com/World/Asia-South-Central/2014/0323/"
            "Tackling-Indian-maternal-deaths-by-smartphone",
        date=date(2014, 4, 23),
    ),
]
