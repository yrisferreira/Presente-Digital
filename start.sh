#!/bin/bash
PORT=${PORT:-5000}
gunicorn app_meupresente:app --bind 0.0.0.0:$PORT --workers 1 --timeout 120
