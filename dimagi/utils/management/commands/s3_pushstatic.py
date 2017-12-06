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
            self.push_file(path)

    def push_file(self, path):
        """
        Push file at path to S3.
        """
        prefixed_path = path.replace(self.staticfiles_dir, '').lstrip('/')
        exists = self.storage.exists(prefixed_path)
        is_js_lib = prefixed_path.startswith('js/lib')

        if not exists:
            print("* Pushing to S3: '%s'" % prefixed_path)
            self.storage.save(prefixed_path, self.local_storage.open(prefixed_path))
        elif exists and not is_js_lib:
            print("- Updating existing file on S3: '%s'" % prefixed_path)
            self.storage.delete(prefixed_path)
            self.storage.save(prefixed_path, self.local_storage.open(prefixed_path))
