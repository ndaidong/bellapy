#!/bin/bash

echo "INFO: cleaning trash files..."
rm -vrf storage ./build ./dist .coverage ./*.pyc ./*.tgz ./*.egg-info ./*__pycache__ .pytest_cache
echo "FINISHED"
