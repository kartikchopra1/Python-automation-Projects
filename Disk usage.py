import shutil
du = shutil.disk_usage("/")
dc = du.free/du.total*100
print(du)
print(dc)
