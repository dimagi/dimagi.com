from dimagi.data.sectors.sector import all_sectors


def get_sector_by_slug(slug):
    sector_by_slug = dict((t.SECTOR.slug, t.SECTOR) for t in all_sectors)
    return sector_by_slug.get(slug)


def get_sectors_page(page):
    first_index = (page - 1) * 20
    last_index = max(first_index + 20, len(all_sectors))

    if last_index > first_index:
        page_sectors = all_sectors[first_index:last_index]
        return [t.SECTOR for t in page_sectors]
