name="nate"
blank = open(f"{name}.txt","r", encoding="utf-8").read().split()
withdrawal  = int(input("How much money would you like to take?:"))
amount= int(blank[11])-withdrawal
blank[11] = str(amount)
print(amount)

update = " ".join(blank)

print(update)

open(f"{name}.txt","w", encoding="utf-8").write(update)

print(f"You withdrew {withdrawal} and you now have £{amount} in your account")
