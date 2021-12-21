release: ./release_tasks.sh
web: gunicorn dimagi.wsgi --timeout 15 --keep-alive 5 --log-level debug --log-file - 
