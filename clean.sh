#!/bin/bash

echo "INFO: cleaning trash files..."
rm -vrf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info
echo "FINISHED"
