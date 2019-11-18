from collections import namedtuple

def latestPartners(data):
    latestPartner = namedtuple('latestPartner', ['title', 'slug', 'excerpt'])
    return [latestPartner(title=partner['title'], slug=partner['slug'], excerpt=partner['excerpt']) for partner in data]
