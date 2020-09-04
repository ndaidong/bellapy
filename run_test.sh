#!/bin/bash

mkdir ./ptester
poetry run flake8 ./ --exclude venv,build,dist --statistics
# poetry run safety check --bare
# ENV=test poetry run pytest --cov-report html --cov=bella tests/*.py
ENV=test poetry run pytest --cov=bella tests/*.py
rm -rf ./ptester
