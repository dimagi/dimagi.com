from __future__ import absolute_import, print_function
import os
import boto3
import time
from django.core.management.base import BaseCommand
from dimagi.storage import S3BotoStorage, StaticFileStorage
from dimagi.utils.config import setting


class Command(BaseCommand):
    help = '''
        Use this to copy files from staticfiles to S3
    '''
    staticfiles_dir = setting('STATIC_ROOT')
    static_url = setting('STATIC_URL')
    cloudfront_distribution_id = setting('AWS_CLOUDFRONT_DISTRIBUTION_ID', '')

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
        self.invalidate_cdn()

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

    def invalidate_cdn(self):
        client = boto3.client('cloudfront')
        invalidation_response = client.create_invalidation(
            DistributionId=self.cloudfront_distribution_id,
            InvalidationBatch={
                'Paths': {
                    'Quantity': 1,
                    'Items': [self.static_url + '*']
                },
                'CallerReference': str(time.time()),
            })
        invalidation_id = invalidation_response['Invalidation']['Id']
        print("-\nCloudFront Invalidation Started: %s" % invalidation_id)
        waiter = client.get_waiter('invalidation_completed')
        print("Waiting for Invalidation to Complete")
        waiter.wait(
            DistributionId=self.cloudfront_distribution_id,
            Id=invalidation_id,
        )
        print("Invalidation Complete. CDN is ready.")
