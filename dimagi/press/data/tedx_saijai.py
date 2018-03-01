from django.utils.translation import ugettext_lazy

from dimagi.press.models import Press

PRESS = Press(
    title=ugettext_lazy(
        "How technology and empathy can change lives: "
        "Saijai Liangpunsakul at TEDxAmRing"
    ),
    source=ugettext_lazy(
        "TEDx Talks"
    ),
    url="https://www.youtube.com/watch?v=pVF1hUTVZ0w",
)
