from __future__ import absolute_import, print_function

import os
from PIL import Image
from django.core.management.base import BaseCommand
from django.contrib.staticfiles import finders


THUMBNAIL_DIR = 'thumbnails'


class Command(BaseCommand):
    help = '''
        Build thumbnails
    '''

    def handle(self, **options):
        print("Building Thumbnails")

        prefix = os.getcwd()

        for finder in finders.get_finders():
            for path, storage in finder.list(['.*', '*~', '* *']):
                if not storage.location.startswith(prefix):
                    continue
                if path.endswith('.jpg') or path.endswith('.png'):
                    source = os.path.join(storage.location, path)
                    dest = os.path.join(storage.location, THUMBNAIL_DIR, path)
                    self.make_thumbnail(source, dest)

    def make_thumbnail(self, source, dest):
        im = Image.open(source)
        im.thumbnail((200, 200), Image.ANTIALIAS)

        dest_dir = "/".join(dest.split('/')[:-1])
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        im.save(dest, "PNG")
