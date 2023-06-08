#! /bin/sh

# Format any errors from *.err files and add them to errors.log
python ./stderr_mon/formatErrors.py

# If errors found, email them
if [ "$(cat errors.log)" != ""];then
  echo "Found errors. Emailing..."
  python ./stderr_mon/email-errors.py
else
  echo "No errors"
fi
