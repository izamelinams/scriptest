import subprocess as cmd
import os
import time 

cp = cmd.run("git add .", check=True, shell=True)
#print(cp)

print("Running")

timesp = str(int(time.time()))
message = "git commit -m 'Update the database {}'".format(timesp)
cp = cmd.run(message,check=True,shell=True)
#cp = cmd.run(f"git commit -m '{message}'", check=True, shell=True)
cp = cmd.run("git push -u origin master -f", check=True, shell=True)
print("hi")
