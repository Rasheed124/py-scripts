
#!/usr/bin/env bash

# Stop immediately if any command fails
set -o errexit

# Explicitly use production settings
export DJANGO_SETTINGS_MODULE=config.settings.production

# Install project dependencies
pip install -r requirements.txt

# Collect production static files using WhiteNoise
python manage.py collectstatic --noinput
