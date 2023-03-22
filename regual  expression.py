# ----------------------- without regular expression indexing ------------
import re
log = "date computer name bad_process[12345]: Error Performance"
index = log.index("[")
print(log[index+1:index+6])  # for know number of char without re

# ------------------------------with re indexing ----------------
log = "date computer name bad_process[12345]: Error Performance"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])


# ------------------------------with re searching ----------------
result = re.search(r"aza", "plaza")
print(result)

# ------------------------------with re searching value . ----------------

print(re.search(r"p.ng", "sponge"))

# ------------------------with re searching value ignore case-----------

print(re.search(r"p.ng", "pangaea", re.IGNORECASE))

# ------------with re searching value lower and upper case -----------

print(re.search(r"[Pp]ython", "Python"))

# ------------with re searching value a-z -----------
print(re.search(r"[a-z]way", "The end of the highway"))
print(re.search(r"[a-zA-Z0-9]way", "The end of the highway"))

# ------------with re searching value not character -----------
print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces"))
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))

# ------------with re searching value differentiated with | -----------
print(re.search(r"cat|dog", "I like both dogs and cats"))

# ------------ re searching repeated mothods| -----------

print(re.search(r"py.*n", "pygmalion"))
print(re.search(r"py.*n", "python programming"))
print(re.search(r"py[a-z].*n", "python programming"))
print(re.search(r"o+l+", "goldfish"))

# ------------ re searching ? as optional -----------
print(re.search(r"p?each", "To each their own"))

# ------------ re searching excape charator -----------
print(re.search(r"\.com", "Vibin.com"))

# ------------ re searching until space-----------
print(re.search(r"\w*", "This is an example"))
print(re.search(r"\w*", "This_is_an_example"))

# --------------Extract PID----------------------


def extract_pid(log_line):
    regex = r"\[(\d+)\]"
    result = re.search(regex, log_line)
    if result is None:
        return ""
    return result[1]


print(extract_pid(log))


# --------------re Split ----------------------
re.split(r"[.!?]", "one Sentence. Another one? and the last one! ")
# --------------re log file  ----------------------
#  Question
#  We're using the same syslog, and we want to display the date, time, and process
#  id that's inside the square brackets. We can read each line of the syslog and
#  pass the contents to the show_time_of_pid function. Fill in the gaps to extract
#  the date, time, and process id from the passed line, and return this format:
#  Jul 6 14:01:23 pid:29440.


def show_time_of_pid(line):
    pattern = r'^(\w+ [0-9] [0-9]+:[0-9]+:[0-9]+) [\w\.]+ [\w=]+\[([0-9]+)\]'
    result = re.search(pattern, line)
    return '{} pid:{}'.format(result[1], result[2])


# Jul 6 14:01:23 pid:29440
print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)"))

# Jul 6 14:02:08 pid:29187
print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)"))

# Jul 6 14:02:09 pid:29187
print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)"))

# Jul 6 14:03:01 pid:29440
print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)"))

# Jul 6 14:03:40 pid:29807
print(show_time_of_pid(
    "Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\""))

# Jul 6 14:04:01 pid:29440
print(show_time_of_pid("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)"))

# Jul 6 14:05:01 pid:29440
print(show_time_of_pid("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)"))
