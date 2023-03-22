#   -------------------------Reading_CSV-------------------------

import csv
f = open("csv_file.txt")
csv_f = csv.reader(f)
for row in csv_f:
    name, phone, role = row  # unpacking the values
    print("name: {}, Phone: {}, Role:{}".format(name, phone, role))
    f.close()


#  -------------------------Genrating_CSV---------------------

hosts = [["workstation.local", " 192.168.25.46"], ["server.cloud", " 1.8.1.2"]]
with open('hosts.csv', 'w') as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)

#  -------------------------W and R CSV with dictionary ---------
with open('softwar.csv') as software:
    reader = csv.DictReader(software)
    for row in reader:
        print(("{} has {} users").format(row["name"], row["users"]))


#  -------------------------W and R CSV with dictionary ---------
users = {"name": "sol Mansi", "username": "solm", "department": "IT"}
{"name": "ssi", "username": "solx", "department": "HR"}
{"name": "sosi", "username": "aola", "department": "DEV ops"}
keys = ["name", "username", "department"]
with open('by_department.csv', 'w') as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.weiteheader()
    writer.writerows(users)
