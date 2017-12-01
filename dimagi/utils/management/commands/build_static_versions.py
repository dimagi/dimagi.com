from __future__ import absolute_import, print_function
import hashlib
import json
import os
from django.core.management.base import BaseCommand
from django.contrib.staticfiles import finders
from django.conf import settings


class Command(BaseCommand):
    help = u"Prints the paths of all the static files to static_versions.py"

    root_dir = settings.PROJECT_ROOT

    def output_resources(self, resources):
        with open(os.path.join(self.root_dir, u'static_versions.py'), 'w') as fout:
            fout.write(u"static_versions = %s" % json.dumps(resources, indent=2))

    def handle(self, **options):
        prefix = os.getcwd()
        resources = {}
        for finder in finders.get_finders():
            for path, storage in finder.list(['.*', '*~', '* *']):
                if not storage.location.startswith(prefix):
                    continue
                if not getattr(storage, 'prefix', None):
                    url = path
                else:
                    url = os.path.join(storage.prefix, path)
                filename = os.path.join(storage.location, path)
                resources[url] = self.get_hash(filename)
        self.output_resources(resources)

    def get_hash(self, filename):
        with open(filename, encoding='utf-8') as f:
            file_hash = hashlib.sha1(f.read().encode('utf-8')).hexdigest()[:7]
        return file_hash
