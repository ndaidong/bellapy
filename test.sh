#!/bin/bash
poetry run flake8 ./ --exclude venv,build,dist --statistics
mkdir storage
poetry run pytest --cov=bella test.py
rm -rf storage
