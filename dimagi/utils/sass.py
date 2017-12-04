from __future__ import absolute_import, print_function
from urllib.parse import urljoin, quote
from sass_processor.processor import SassProcessor
from django.templatetags.static import PrefixNode


class CDNSassProcessor(SassProcessor):

    @classmethod
    def handle_simple(cls, path):
        return urljoin(PrefixNode.handle_simple('STATIC_URL'), quote(path))
