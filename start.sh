#! /bin/sh

cd /thisAutomation
echo > errors.log

python automation.py 2>automation.py.err

python ./stderr_mon/errorHandler.sh
