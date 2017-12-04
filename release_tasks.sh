#!/bin/sh

rm -r ./staticfiles
python manage.py compilescss
python manage.py collectstatic --ignore=*.scss --clear --no-input
rm static_versions.py
python manage.py build_static_versions
python manage.py compilescss --delete-files
