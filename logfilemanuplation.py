#  --------------Print out user name from log-----------------------------
import re
import sys

logfile = sys.argv[1]
with open(logfile) as f:
    for line in f:
        if "CRON" not in line:
            continue
        pattern = r"USER \((\w+)\)$"
        result = re.search(pattern, line)
        print(result[1])
#  --------------Print out user name from log and their count--------------


logfile = sys.argv[1]
usernames = {}
with open(logfile) as f:
    if "CRON" not in line:
        continue
    pattern = r"USER \((\w+)\)$"
    result = re.search(pattern, line)
    if result is None:
        continue
    name = result[1]
    usernames[name] = usernames.get(name, 0) + 1
