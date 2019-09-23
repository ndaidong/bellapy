#!/bin/bash
flake8 ./ --exclude venv,build,dist --statistics
safety check --bare
pytest --cov=bella test.py
