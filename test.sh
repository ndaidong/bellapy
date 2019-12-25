#!/bin/bash
flake8 ./ --exclude venv,build,dist --statistics
safety check --bare
mkdir storage
pytest --cov=bella test.py
rm -rf storage
