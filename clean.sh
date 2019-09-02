#!/bin/bash

echo "INFO: cleaning trash files..."
rm -vrf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info ./*__pycache__ .pytest_cache
echo "FINISHED"
