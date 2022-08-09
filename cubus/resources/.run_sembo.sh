#!/bin/bash

# Unzip sembo app if not already done
if test -f sembo.zip; then
  unzip sembo.zip
  rm -f sembo.zip
  pip install -r sembo_app/requirements.txt
fi

# Run sembo on the background
python3 sembo_app/app.py &

