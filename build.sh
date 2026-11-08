
#!/usr/bin/env bash

# Stop immediately if any command fails
set -o errexit

# Install project dependencies
pip install -r requirements.txt

# Collect production static files
python manage.py collectstatic --noinput
