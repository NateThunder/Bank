import os
import time
name = "nate"
blank = open(f"{name}.txt","r", encoding="utf-8").read().split()
history = []
while True:
    try:
        withdrawal  = float(input("How much money would you like to take?: £"))
        figure = str(withdrawal).split(".")

        if len(figure[1]) <= 2:# Checking for 2 decimal places
            print(figure)
            break
        else:
            print("Your amount can not have more than 2 decimal places e.g £55.55")
            time.sleep(2)
            #os.system("cls")
    except:
        print("You have to enter a vailid input like '234.34'! ")
        time.sleep(2)
#--------------------------------------------- Is there enough money in the account -----------------------------------------------
if float(withdrawal)> float(blank[11])+float(blank[8]) :
    form = round(float(blank[11])+float(blank[8]),2)
    available = f"{form:.2f}"
    print(f"You onle have £{float(blank[11]):.2f} in your accout and your overdraft is £{float(blank[8]):.2f}, you can not withdraw {withdrawal}!\n"
            f"You can withdraw £{float(available):2f} or less")

#----------------------------------------------- There is enough in your account --------------------------------------------------
else:
    amount= float(blank[11])-withdrawal
    history.append(f"-{amount}")
    print(history)
    blank[11] = str(amount)
    blank[14] = str(history)

    update = " ".join(blank)
    open(f"{name}.txt","w", encoding="utf-8").write(update)
    print(f"You withdrew {float(withdrawal):.2f} and you now have £{float(amount):.2f} in your account")