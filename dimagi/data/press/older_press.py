from datetime import date
from django.utils.translation import ugettext_lazy

from dimagi.pages.models.press import Press

PRESS = [
    Press(
        title=ugettext_lazy(
            "Ubiquitous Across Globe, Cellphones Have Become Tool for "
            "Doing Good"
        ),
        source=ugettext_lazy(
            "New York Times"
        ),
        url="http://www.nytimes.com/2013/11/08/giving/ubiquitous-across-"
            "globe-cellphones-have-become-tool-for-doing-good.html",
        date=date(2013, 11, 8),
    ),
    Press(
        title=ugettext_lazy(
            "Small business advice: How to run a social enterprise"
        ),
        source=ugettext_lazy(
            "The Washington Post"
        ),
        url="https://www.washingtonpost.com/blogs/on-small-business/post/"
            "small-business-advice-how-to-run-a-social-enterprise/2013/"
            "09/27/016b670c-2778-11e3-b75d-5b7f66349852_blog.html"
            "?utm_term=.008a9971db7a",
        date=date(2013, 9, 27),
    ),
    Press(
        title=ugettext_lazy(
            "TBI Social Enterprises: Dimagi – Applying Intelligence And "
            "Innovation To Health Care Solutions"
        ),
        source=ugettext_lazy(
            "The Better India"
        ),
        url="https://www.thebetterindia.com/8173/tbi-social-enterprises-"
            "dimagi-applying-intelligence-and-innovation-to-health-care-"
            "solutions/",
        date=date(2013, 9, 13),
    ),
    Press(
        title=ugettext_lazy(
            "Can Silicon Valley Save the World?"
        ),
        source=ugettext_lazy(
            "Foreign Policy"
        ),
        url="http://foreignpolicy.com/2013/06/24/can-silicon-valley-save-"
            "the-world/",
        date=date(2013, 6, 24),
    ),
    Press(
        title=ugettext_lazy(
            "YEC Member Spotlight: Jonathan Jackson, CEO, Dimagi"
        ),
        source=ugettext_lazy(
            "Business Insider"
        ),
        url="http://www.businessinsider.com/yec-member-spotlight-jonathan-"
            "jackson-ceo-dimagi-2013-4",
        date=date(2013, 4, 23),
    ),
    Press(
        title=ugettext_lazy(
            "Can Empathy Scale Technology?"
        ),
        source=ugettext_lazy(
            "Huffington Post"
        ),
        url="https://www.huffingtonpost.com/jonathanjackson/can-empathy-"
            "scale-technol_b_2900890.html",
        date=date(2013, 3, 18),
    ),
    Press(
        title=ugettext_lazy(
            "CommCare Helps Pregnant Kenyan Women Save Money, Pre-pay For "
            "Their Delivery"
        ),
        source=ugettext_lazy(
            "NetHope"
        ),
        url="https://solutionscenter.nethope.org/resources/commcare-helps-"
            "pregnant-kenyan-women-save-money-pre-pay-for-their-delivery",
        date=date(2013, 3, 12),
    ),
    Press(
        title=ugettext_lazy(
            "Scaling CommCare"
        ),
        source=ugettext_lazy(
            "USAID"
        ),
        url="https://www.usaid.gov/div/commcare",
        date=date(2013, 2, 15),
    ),
    Press(
        title=ugettext_lazy(
            "Massachusetts companies create socially responsible "
            "'benefit corporations'"
        ),
        source=ugettext_lazy(
            "MassLive"
        ),
        url="http://www.masslive.com/politics/index.ssf/2012/12/"
            "massachusetts_companies_create.html",
        date=date(2012, 12, 4),
    ),
    Press(
        title=ugettext_lazy(
            "Can the new “benefit corporation” charters give companies "
            "a conscience?"
        ),
        source=ugettext_lazy(
            "Boston Globe"
        ),
        url="https://www.bostonglobe.com/ideas/2012/11/25/virtue-inc/"
            "sMNhJRcOIgZ0rqjpLTALrN/story.html",
        date=date(2012, 11, 25),
    ),
    Press(
        title=ugettext_lazy(
            "Letting Employees Work Remotely Pays Off"
        ),
        source=ugettext_lazy(
            "Inc."
        ),
        url="https://www.inc.com/magazine/201210/adam-bluestein/"
            "letting-employees-work-remotely-pays-off.html",
        date=date(2012, 9, 25),
    ),
    Press(
        title=ugettext_lazy(
            "The Future of mHealth"
        ),
        source=ugettext_lazy(
            "PLOS Global Health"
        ),
        url="http://blogs.plos.org/globalhealth/2017/03/%EF%BB%BFthe-"
            "future-of-mhealth/",
        date=date(2012, 4, 22),
    ),
    Press(
        title=ugettext_lazy(
            "Norway Commits $9.9 Million to Maternal and Newborn Health"
        ),
        source=ugettext_lazy(
            "PR Newswire"
        ),
        url="http://www.prweb.com/releases/mhealth/alliance/prweb9254025.htm",
        date=date(2012, 3, 5),
    ),
    Press(
        title=ugettext_lazy(
            "Building innovation in India"
        ),
        source=ugettext_lazy(
            "MIT News"
        ),
        url="http://news.mit.edu/2011/india-conference-0927",
        date=date(2011, 9, 27),
    ),
    Press(
        title=ugettext_lazy(
            "Saving the World on a Shoestring: Spark MicroGrants"
        ),
        source=ugettext_lazy(
            "Forbes"
        ),
        url="https://www.forbes.com/sites/susanadams/2011/07/11/saving-"
            "the-world-on-a-shoestring-spark-microgrants/#3a3784e240c6",
        date=date(2011, 7, 11),
    ),
    Press(
        title=ugettext_lazy(
            "Global Indian of the Year"
        ),
        source=ugettext_lazy(
            "The Times of India"
        ),
        url="https://timesofindia.indiatimes.com/india/Global-Indian-"
            "of-the-Year/articleshow/1337920.cms",
        date=date(2005, 12, 19),
    ),
]
