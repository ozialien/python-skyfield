#!/bin/bash

if conda --version >/dev/null 2>&1
then
    conda install -file requirements.txt
fi
pip install -e .
