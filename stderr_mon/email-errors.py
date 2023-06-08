import os, sys, configparser
from custom_internal_email_sending_module_not_included import Email

# If error log is empty, exit.
if os.path.getsize("errors.log") == 0:
    print("No Errors")
    sys.exit(0)

# Read config (located in automation folder with start.sh)
config = configparser.ConfigParser()
config.read('stderr_mon.conf')

# Pull config values out to shorter variables.
automation_name = config['stderr_mon']['automation_name'].replace('"', '')
notification_email = config['stderr_mon']['notification_email'].replace('"', '')
try:
    # Help text optional
    helptext = '<b>Info:</b>&nbsp;'+config['stderr_mon']['helptext'].replace('"', '').replace('\n', '<br>').replace('  ', '&nbsp;&nbsp;')    
except:
    helptext = ""

# HTMLify any newlines and spaces in the error log
with open('errors.log', 'r') as f:
    errors = f.read().replace('\n', '<br>').replace('  ', '&nbsp;&nbsp;')

# Build and send notification email
mail = Email("ExampleErrorNotificationEmailSender@company.org", notification_email)
mail.subject = f"Automation - {automation_name} - Error"
mail.content = errors + helptext
mail.send()
