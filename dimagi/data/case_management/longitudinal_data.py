from __future__ import absolute_import
from collections import namedtuple
from django.utils.translation import ugettext_lazy

TableRow = namedtuple(
    'TableRow', 'title survey case'
)

TABLE = [
    TableRow(
        ugettext_lazy("Store previously collected data on mobile devices"),
        False, True
    ),
    TableRow(
        ugettext_lazy("Analyze individual survey form responses"),
        True, True
    ),
    TableRow(
        ugettext_lazy("Aggregate data from relevant survey forms into cases"),
        False, True
    ),
    TableRow(
        ugettext_lazy("Employ skip logic to customize forms"),
        True, True
    ),
    TableRow(
        ugettext_lazy("Use existing case data to ask contextual questions"),
        False, True
    ),
    TableRow(
        ugettext_lazy("View historical case information offline"),
        False, True
    ),
    TableRow(
        ugettext_lazy("Share cases and refer subjects to other CommCare users"),
        False, True
    ),
    TableRow(
        ugettext_lazy("Provide simple counseling messages"),
        True, True
    ),
    TableRow(
        ugettext_lazy("Display dynamic advice based on a case’s history"),
        False, True
    ),
    TableRow(
        ugettext_lazy("Manually trigger referrals"),
        True, True
    ),
    TableRow(
        ugettext_lazy("Send SMS messages when cases meet a given set "
                      "of conditions"),
        False, True
    ),
]
