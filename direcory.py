#   ----- Current_directory------------------

import os
print(os.getcwd())

#    ----------------------New_directory-----------------------

os.mkdr("new_dir")


#    ----------------------Change_directory-----------------------

os.chdir("new_dir")


#    ----------------------remove_directory-----------------------

os.rmdir("new_dir")


#    ----------------------List_directory-----------------------

os.listdir("website")

#    ----------------------List_directory_type-----------------------

dir = website
for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))

#       Response:
#   website/images is a directory
#   website/index.html is a file
#    website/favicon.ico is a file -
