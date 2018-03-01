from dimagi.press.data import press


def get_press_page(page):
    first_index = (page - 1) * 20
    last_index = max(first_index + 20, len(press))

    if last_index > first_index:
        page_press = press[first_index:last_index]
        return [t.PRESS for t in page_press]
