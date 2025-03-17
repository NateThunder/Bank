import os
import time
name = "nate"
blank = open(f"{name}.txt","r", encoding="utf-8").read().split()
overdraft = input("What would you like your overdraft to be?: £")
blank[8]=str(overdraft)
update = " ".join(blank)
open(f"{name}.txt","w", encoding="utf-8").write(update)
os.system("cls")
print(f"Your overdraft is now {blank[8]}, that's Dope A F. Remember it is not free money. Enjoy!")
print(blank)