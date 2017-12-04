from __future__ import absolute_import
from storages.backends.s3boto3 import S3Boto3Storage
from dimagi.utils.config import setting
from django.core.files.storage import get_storage_class
from sass_processor.storage import SassS3Boto3Storage

STATIC_URL = setting('STATIC_URL', '')
STATIC_CDN = setting('STATIC_CDN', '')
CDN_BASE_URL = STATIC_CDN + STATIC_URL

B3_ROOT_LOCATION = setting('AWS_LOCATION', STATIC_URL)


class CachedS3BotoStorage(SassS3Boto3Storage):
    """
    S3 storage backend that saves the files locally, too.
    """
    location = STATIC_URL
    base_url = CDN_BASE_URL

    def __init__(self, *args, **kwargs):
        super(CachedS3BotoStorage, self).__init__(*args, **kwargs)
        self.local_storage = get_storage_class(
            "compressor.storage.CompressorFileStorage")()

    def _save(self, name, content):
        self.local_storage._save(name, content)
        super(CachedS3BotoStorage, self)._save(name, self.local_storage._open(name))
        return name

    def rename(self, src_key, dest_key, delete_source=False):
        if self.exists(dest_key):
            self.bucket.Object(dest_key).delete()
        self.connection.meta.client.copy({
            'Bucket': self.bucket_name,
            'Key': src_key
        }, self.bucket_name, dest_key)
        if delete_source:
            self.bucket.Object(src_key).delete()

