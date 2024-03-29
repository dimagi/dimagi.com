from __future__ import absolute_import, print_function
import os
import boto3
import time
import subprocess
from dimagi.utils.management.commands.s3_pushstatic import Command as PushStaticCommand
from dimagi.storage import S3BotoStorage, StaticFileStorage
from dimagi.utils.config import setting
from dimagi.utils.environment import is_production_environment


class Command(PushStaticCommand):
    help = '''
        Use this to sync images from a non-master branch with S3
    '''

    def add_arguments(self, parser):
        parser.add_argument(
            '-c',
            '--changes',
            action='store_true',
            dest='changes',
            help='Only push changed files',
        )

    def handle(self, **options):
        only_changes = options["changes"]
        if only_changes:
            output = subprocess.Popen(
                "git diff master --name-only", shell=True, stdout=subprocess.PIPE, universal_newlines=True
            )
            changed_images = [s.replace('dimagi/pages/static/', '') for s in output.stdout.read().split('\n')
                              if 'static' in s and not (s.endswith('.scss') or s.endswith('.js'))]
        else:
            changed_images = []
        files_to_push = []
        for (dirpath, dirnames, filenames) in os.walk(self.staticfiles_dir):
            filepaths = [os.path.join(dirpath, f) for f in filenames]
            files_to_push.extend(filepaths)

        for path in files_to_push:
            if (path.endswith('.jpg') or path.endswith('.png')) and \
                    (not only_changes or any(p in path for p in changed_images)):
                self.push_file(path)
        if is_production_environment():
            self.invalidate_cdn()
