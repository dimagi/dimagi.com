from __future__ import absolute_import, print_function
from urllib.parse import urljoin, quote
from sass_processor.processor import SassProcessor
from django.templatetags.static import PrefixNode
from sass_processor.templatetags.sass_tags import SassSrcNode


class CDNSassProcessor(SassProcessor):
    @classmethod
    def handle_simple(cls, path):
        return urljoin(PrefixNode.handle_simple('STATIC_URL'), quote(path))


class CDNSassSrcNode(SassSrcNode):
    def __init__(self, path):
        self.sass_processor = CDNSassProcessor(path)
