#!/bin/sh

python manage.py build_thumbnails
python manage.py collectstatic --clear --no-input
python manage.py s3_sync_images
