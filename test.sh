#!/bin/bash

pycodestyle ./ --exclude venv --statistics
safety check --bare
pytest --cov=bella test.py
