from __future__ import absolute_import, print_function
import os
from django.core.management.base import BaseCommand
from dimagi.storage import S3BotoStorage, StaticFileStorage
from dimagi.utils.config import setting


class Command(BaseCommand):
    help = '''
        Use this to copy files from staticfiles to S3
    '''
    staticfiles_dir = setting('STATIC_ROOT')

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.storage = S3BotoStorage()
        self.local_storage = StaticFileStorage()

    def handle(self, **options):
        files_to_push = []
        for (dirpath, dirnames, filenames) in os.walk(self.staticfiles_dir):
            filepaths = [os.path.join(dirpath, f) for f in filenames]
            files_to_push.extend(filepaths)

        for path in files_to_push:
            self.copy_file(path)

    def copy_file(self, path):
        """
        Attempt to copy ``path`` with storage
        """
        prefixed_path = path.replace(self.staticfiles_dir, '').lstrip('/')
        print("Copying '%s'" % path)
        self.storage.save(prefixed_path, self.local_storage.open(prefixed_path))
