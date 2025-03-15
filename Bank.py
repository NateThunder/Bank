import os
#-------------------------------- Welcome message -------------------------------------------------------------------------
print("Welcome to Dope A F bank. The home of your banking needs ")

#------------------------------ Log into your bank ------------------------------------------------------------------------

#-------------------------- Do you have an account? -----------------------------------------------------------------------
def main():
    os.system("cls")
    start = input("Do you have an account. Please type Y for Yes and N for No. ").capitalize().strip()
    os.system("cls")
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
        n =3
        while n >0:            
            if start == "Y":
                try: 
                    while n == 3:
                        print("OK lets Log into your Dope A F bank account \n")
                        break
                    name = input("Please enter your user name ")
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
    print(f"You have £{blank[11]} in your account")
    while True:
        option = input("Type W if you want to withdraw money or type D to deposit money?: ").lower() #withdraw or deposit
#---------------------------- Withdrawal ----------------------------------------------------------    
        if option == "w":
            withdrawal  = int(input("How much money would you like to take?: "))
            amount= int(blank[11])-withdrawal
            blank[11] = str(amount)
            update = " ".join(blank)
            open(f"{name}.txt","w", encoding="utf-8").write(update)
            print(f"You withdrew {withdrawal} and you now have £{amount} in your account")
#--------------------- Deposit -----------------------------------------------------------------------
        elif option == "d":
            deposit  = int(input("How much money would you like to deposit?: "))
            amount= int(blank[11])+deposit
            blank[11] = str(amount)
            update = " ".join(blank)
            open(f"{name}.txt","w", encoding="utf-8").write(update)
            print(f"You deposited {deposit} and you now have £{amount} in your account")

        done  = input("Would you like anything else. Y for Yes and N for No: ").upper()
        if done == "N":
            print("Thank you for using Dope A F. Goodbye 👋🏾 ")
            main()


#------------------- Text file created for new customer -------------------------------------------------
def customer_file(inname, inpin):
    file_name= f"{inname}.txt"
    open(file_name, "w", encoding="utf-8").write(f"Name = {inname} Pin = {inpin} Overdraft = 0 Total = 0 Transactions = 0")

main()