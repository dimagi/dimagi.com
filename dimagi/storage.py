from __future__ import absolute_import

from require.storage import OptimizedFilesMixin
from storages.backends.s3boto3 import S3Boto3Storage

from dimagi.utils.config import setting
from sass_processor.storage import SassFileStorage
from compressor.storage import CompressorFileStorage

STATIC_URL = setting('STATIC_URL', '')
STATIC_CDN = setting('STATIC_CDN', '')
CDN_BASE_URL = STATIC_CDN + STATIC_URL


class StaticFileStorage(OptimizedFilesMixin, SassFileStorage):
    pass


class SassS3Boto3Storage(S3Boto3Storage):
    base_url = '{}.s3.amazonaws.com'.format(setting('AWS_STORAGE_BUCKET_NAME', ''))


class S3BotoStorage(SassS3Boto3Storage):
    """
    S3 storage backend that has the right locations
    """
    location = STATIC_URL.lstrip("/")
    base_url = CDN_BASE_URL


class CompressedFileStorage(CompressorFileStorage):
    base_url = STATIC_URL


class CachedS3BotoStorage(S3BotoStorage):

    def __init__(self, *args, **kwargs):
        super(CachedS3BotoStorage, self).__init__(*args, **kwargs)
        self.local_storage = CompressedFileStorage()

    def _save(self, name, content):
        self.local_storage._save(name, content)
        super(S3BotoStorage, self)._save(name, self.local_storage._open(name))
        return name
