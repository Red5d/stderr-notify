# stderr_mon

A set of example scripts for building an automation monitoring solution.

To use,
1. Clone this repo
2. Add your automation script
3. Edit start.sh to run your script instead of "automation.py" and change "thisAutomation" to whatever you name the folder instead of "stderr-notify"
4. Edit stderr_mon/handleErrors.sh to run your notification script instead of "email-errors.py"
5. Edit stderr_mon.conf and change the three notification information values to ones that make sense for your automation.
6. Run the automation in a docker container as shown below, replacing the paths and image name with your own.

> docker run --rm -v /path/to/thisAutomation:/thisAutomation <docker_image_name> /thisAutomation/start.sh
