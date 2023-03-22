# file management --------------REMOVE FILE---------------

import datetime
import os
os.remove("novel.txt")

#  ---------------------------Rename file------------------------
os.rename("first_draft.txt", "finished_masterpiece.txt")

#  --------------------------path exist----Response(T/F)--------------------

os.path.exists("finished_masterpiece.txt")

#  -----------------------------file Size------------------------------
os.path.getsize("masterpiece.txt")

# ---------------------timestamp-----------------------------------
os.path.getmtime("Dragon.txt")
#  -----
timestamp = os.path.getmtime("Spider.txt")
datetime.datetime.fromtimestamp(timestamp)

# ------------------------------------path of file--------------------

os.path.abspath("smart.txt")
