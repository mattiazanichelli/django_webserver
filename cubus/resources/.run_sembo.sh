#!/bin/bash

# Unzip sembo app if not already done
if test -f sembo.zip; then
  unzip sembo.zip
  rm sembo.zip -y
  pip install -r sembo_app/requirements.txt
fi

# Run sembo on the background
python3 sembo_app/app.py &

