from dimagi.data.quick_start.areas import all_areas


def get_area_by_slug(slug):
    area_by_slug = dict((a.AREA.slug, a.AREA) for a in all_areas)
    return area_by_slug.get(slug)
