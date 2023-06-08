import sys

# Find scripts in start.sh that have stderr redirection
scripts = []
with open('start.sh', 'r') as f:
    for line in f.readlines():
        if '2>' in line:
            scripts.append(line.split('2>')[1].split('.err')[0])

# List of non-error partial line matches to exclude
exclusions = [
    'DeprecationWarning',
    'InsecureRequestWarning'
]

for script in scripts:
    errorlines = []
    
    # For each script, check its *.err file for error messages
    with open(script+'.err', 'r') as err:
        # For each line in the .err file, filter each line with the list of exclusions.
        for line in err.readlines():
            if not any(e in line for e in exclusions):
                errorlines.append(line)
            
    # If any lines are left, write them to the error log with some HTMl formatting around them.
    if len(errorlines) > 0:
        with open('errors.log', 'a') as f:
            f.write(f"<b>Error in {script}:</b>\n")
            f.writelines(errorlines)
            f.write("<br><br>\n")
