#!/usr/bin/python3
# parse keystone.common.wsgi and return number of failed login attempts

# Track failed login attempts
failedLogins = 0

# Open log file
logFile = open("/home/student/mycode/attemptlogin/keystone.common.wsgi", "r")

# Read log file into memory
logText = logFile.readlines()

# Use loop to look for failed logins
for logLine in logText:
    # Look for failed logins based on log text
    if "- - - - -] Authorization failed"  in logLine:
        failedLogins += 1
print("Failed login attempts: ", failedLogins)

logFile.close()


