#!/bin/bash

flake8 ./ --exclude venv --statistics
safety check --bare
pytest --cov=bella test.py
