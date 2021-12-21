release: ./release_tasks.sh
web: gunicorn dimagi.wsgi --log-file --timeout 15 --keep-alive 5 --log-level debug
