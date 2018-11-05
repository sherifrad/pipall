# coding: utf-8

import subprocess
import re

cmd = ['pip', 'freeze']
process = subprocess.check_output(cmd).decode('utf-8')
# list of packages with version eg: ['alembi==1.0.0', 'sqlalchemy==1.3.1']
prcs_result = process.split('\n')
pkgs = []  # packages list without version. eg: ['alembi', 'sqlalchemy']
pattern = "[^=]*"

notify = """
            ======================================
            =        Collecting Packages         =       
            ======================================"""
print(notify)

for i in prcs_result:
    package = re.search(pattern, i).group()
    pkgs.append(package)

notify = """
            ======================================
            =  Packages that will be updated     =       
            ======================================"""
print(notify)
for pkg in prcs_result:
    pkg.lower()
    print(pkg)
prompt = input("Do You Want To Proceed[Y|N]")
if prompt.lower() == 'y':
    print("Startin The Process...")
    for i in pkgs:
        p = subprocess.Popen(['pip', 'install', '-U', i], stdout=subprocess.PIPE)
        stdout, stderr = p.communicate()
        print(stdout.decode('utf-8'), flush=True)
else:
    print("Cancelling The Process")
