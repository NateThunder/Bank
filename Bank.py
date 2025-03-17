import os
import time
#------------------------------ Bank app ------------------------------------------------------------------------
def main():
    os.system("cls")
#-------------------------------- Welcome message -------------------------------------------------------------------------
    print(f"{open(f"Bank_logo.txt","r", encoding="utf-8").read()}" # Print company logo ASCII art                                                                                                                                                                                                                                                                                                             
    "\nWelcome to Dope A F bank. The home of your banking needs \n")
#-------------------------- Do you have an account? -----------------------------------------------------------------------
    start = input("Do you have an account. Please type Y for Yes and N for No. ").capitalize().strip()
    os.system("cls")
    options = ["Y","N"]
    if start not in options:
        print("You have to enter the letter Y or N.")
        time.sleep(1)
        main()
    while True:
        # Register
        if start == "N":
            print("A new customer Great. You will not regret joining Dope A F.\n")
            inname = input("What is your user name ")
            
#--------------- Making sure it is a 4 digit pin -------------------------------------------------------------------------           
            while True:
                try:
                    inpin = int(input("What is your pin "))
                    if len(str(inpin)) == 4: #Change the number to to change length of pin
                        break
                    else:
                        print("Your pin has to be 4 numbers. It can not have letters. No more and no less")

                except: # in case the input is not an int
                    print("Your pin has to be 4 numbers. It can not have letters. No more and no less")
                    continue
#------------------- Write information to a text file --------------------------------------------------------------------
            os.system("cls")
            customer_file(inname, inpin)

            start="Y" # Now user has account           
#-------------------------------------- login ----------------------------------------------------------------------------
#----------------------------------- making sure its 4 attempts -----------------------------------------------------------        
        n =3 # Initialising attempts
        while n >0:            
            if start == "Y":
                try: 
                    while n == 3:
                        print("OK lets Log into your Dope A F bank account \n")
                        break
                    name = input("Please enter your user name ").lower()
                    pin = int(input("Please enter your pin "))
#------------------- Getting user information in files -------------------------------------------------------------------                    
                    fpin = open(f"{name}.txt", "r", encoding="utf-8").read().split()
                    print(f"Password = {fpin[5]}\nName = {fpin[2]}")
                    record_name = fpin[2]
                    record_pin = int(fpin[5])
                    os.system("cls")
#------------------ comparing user information with input -----------------------------------------------------------------

                    if name == record_name and pin == record_pin:
                        print(f"Welcome to your Dope A F account {name.capitalize()}")
                        account(name)
                        break  
                except: # Start again
                    print("The account is not recognised. Try registering for an account")
                    main()            
            else:
                n-=1  # Atempts
                print(f"wrong credential {n} more attempts left.")       
        break
#------------------- Bank acount information -------------------------------------------------------------------------------
def account(name):
    blank = open(f"{name}.txt","r", encoding="utf-8").read().split()
    
    while True:
        print(f"You have £{blank[11]} in your account\n"
              f"Your overdraft is £{blank[8]}")
        option = input("Type W if you want to withdraw money, type D to deposit money or type O to change your overdraft: ").lower() #withdraw or deposit
#---------------------------- Withdrawal ----------------------------------------------------------    
        if option == "w":
            withdrawal  = float(input("How much money would you like to take?: £"))
            os.system("cls")
#--------------------- Is there enough money in the account ----------------------------------------------
            if float(withdrawal)> float(blank[11])+float(blank[8]) :
                print(f"You onle have £{blank[11]} in your accout and your overdraft is £{blank[8]}, you can not withdraw {withdrawal}!\n"
                      f"You can withdraw {float(blank[11])+float(blank[8])} or less")
                continue
#--------------------- There is enough in your account --------------------------------------------------
            else:
                amount= float(blank[11])-withdrawal
                blank[11] = str(amount)
                update = " ".join(blank)
                open(f"{name}.txt","w", encoding="utf-8").write(update)
                print(f"You withdrew {withdrawal} and you now have £{amount} in your account")

#---------------------------------- Deposit --------------------------------------------------------------------
        elif option == "d":
          #  os.system("cls")
            deposit  = float(input("How much money would you like to deposit?: £"))
            os.system("cls")
            amount= int(blank[11])+deposit
            blank[11] = str(amount)
            update = " ".join(blank)
            open(f"{name}.txt","w", encoding="utf-8").write(update)
            print(f"You deposited {deposit} and you now have £{amount} in your account")

#-------------------------- Overdraft ---------------------------------------------------------------------------
        if option == "o":
            overdraft = input("What would you like your overdraft to be?: £")
            blank[8]=str(overdraft)
            update = " ".join(blank)
            open(f"{name}.txt","w", encoding="utf-8").write(update)
            os.system("cls")
            print(f"Your overdraft is now {blank[8]}, that's Dope A F. Remember it is not free money. Enjoy!")

#---------------------------- Ending the system ----------------------------------------------------------------
        done  = input("Would you like anything else. Y for Yes and N for No: ").upper()
        if done == "N":
            os.system("cls")
            print(f"{open("bye.txt","r", encoding="utf-8").read()}" # Print Bye ASCII art from file
            "\nThank you for using Dope A F. Goodbye!")
            time.sleep(2)
            os.system("cls")
            animation(1)
            print(f"{open("piggybank.txt", "r", encoding="utf-8").read()}")
            time.sleep(2)
            main()

#------------------- Text file created for new customer ----------------------------------------------------------
def customer_file(inname, inpin):
    name = inname.lower()
    file_name= f"{name}.txt"
    open(file_name, "w", encoding="utf-8").write(f"Name = {inname} Pin = {inpin} Overdraft = 0 Total = 0 Transactions = 0")

#------------------------------- Stickman Animation -------------------------------------------------------

def animation(length):
    x=0
    for _ in range(length):
        for _ in range(25):
            animation = open(f"frame{x}.txt","r", encoding="utf-8").read()
            x=x+1
            print(animation)
            time.sleep(0.04)
            os.system("cls")
        x=0
main()
