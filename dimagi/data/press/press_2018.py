from datetime import date
from django.utils.translation import ugettext_lazy

from dimagi.pages.models.press import Press

PRESS = [
    Press(
        title=ugettext_lazy(
            "Elastic Announces Recipients of 2018 Elastic Cause Awards"
        ),
        source=ugettext_lazy(
            "Global Newswire"
        ),
        url="https://globenewswire.com/news-release/2018/02/28/1396579/0/en/"
            "Elastic-Announces-Recipients-of-2018-Elastic-Cause-Awards.html",
        date=date(2018, 2, 28),
    ),
    Press(
        title=ugettext_lazy(
            "Kalter: Tufts docs’ app to help drug-exposed newborns"
        ),
        source=ugettext_lazy(
            "Boston Herald"
        ),
        url="http://www.bostonherald.com/news/columnists/lindsay_kalter/2018/"
            "02/kalter_tufts_docs_app_to_help_drug_exposed_newborns",
        date=date(2018, 2, 14),
    ),
]
