import math
from collections import namedtuple

from django.urls import reverse
from django.utils.dateparse import parse_datetime

from dimagi.utils.wordpress_api import url_filters

Category = namedtuple('Category', 'name description icon slug')
CanonicalLink = namedtuple('CanonicalLink', 'slug url')


class BlogPost(object):

    def __init__(self, data):
        self.title = data['title']

        from dimagi.data.blog import get_category_by_slug
        self.category = get_category_by_slug(data['category'])

        self.authors = [Author(a) for a in data['authors']]
        self.tags = [Tag(t) for t in data['tags']]

        self.date = parse_datetime(data['date_gmt'])
        self.slug = data['slug']
        self.thumbnail = data['thumbnail']
        self.wistia = data['wistia']

        self.excerpt = data.get('excerpt')
        self.content = url_filters(data.get('content'))

        self.reading_time_in_minutes = math.ceil(len(self.content.split(' ')) / 300) if self.content else 0

    def __str__(self):
        return "[{category} - {date}] {title}".format(
            category=self.category.slug,
            date=self.date_human,
            title=self.title,
        )

    @property
    def date_human(self):
        return self.date.strftime("%B %-d, %Y")

    @property
    def url(self):
        return reverse('blog_post', args=[self.slug])

    @property
    def canonical_link(self):
        from dimagi.data.blog.canonical import get_canonical_link
        return get_canonical_link(self.slug)

    @property
    def has_multiple_authors(self):
        return len(self.authors) > 1

    @property
    def author(self):
        return self.authors[0]

    @property
    def authors_list(self):
        return ", ".join([a.name for a in self.authors])


class Author(object):

    def __init__(self, data):
        self.image = url_filters(data['image'])
        self.name = data['name']
        self.role = data['role']


class Tag(object):

    def __init__(self, data):
        self.id = data['id']
        self.slug = data['slug']
        self.name = data['name']
        self.total = data['total']
