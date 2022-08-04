#!/bin/sh

python manage.py migrate
python manage.py build_thumbnails
python manage.py compilescss
python manage.py collectstatic --clear --no-input
python manage.py compress
python manage.py build_static_versions
python manage.py compilescss --delete-files
python manage.py s3_pushstatic
