import os
import time

rep  =  open("bank_logo.txt", "r", encoding="utf-8").read()
new = rep.replace("$", "£")
open("pound_logo.txt","w",encoding="utf-8").write(new)
print(new)