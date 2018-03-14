import math

from dimagi.data.press import (
    press_2018,
    press_2017,
    press_2016,
    press_2015,
    press_2014,
    older_press
)


press = (
    press_2018,
    press_2017,
    press_2016,
    press_2015,
    press_2014,
    older_press
)


press_by_date = []
for p in press:
    press_by_date.extend(p.PRESS)

press_by_date.sort(key=lambda x: x.date, reverse=True)


ARTICLES_PER_PAGE = 18
TOTAL_PAGES = math.ceil(len(press_by_date)/ARTICLES_PER_PAGE)


def get_press_page(page):
    first_index = (page - 1) * ARTICLES_PER_PAGE
    last_index = min(first_index + ARTICLES_PER_PAGE, len(press_by_date))

    if last_index > first_index:
        return press_by_date[first_index:last_index]
