import os
#-------------------------------- Welcome message --------------------------------------------------------
print("Welcome to Dope A F bank. The home of your banking needs ")

#------------------------------ Log into your bank --------------------------------------------------------




#-------------------------- Do you have an account? -------------------------------------------------------
def main():
    start = input("Do you have an account. Please type Y for yes and N for No. ").capitalize().strip()
    os.system("cls")
    while True:
        # Register
        if start == "N":
            print("A new customer Great. You will not regret joining Dope A F.\n")
            inname = input("What is your user name ")
            inpin = int(input("What is your pin "))
            os.system("cls")
            customer_file(inname, inpin)
            start="Y"

#-------------------------------------- login -----------------------------------------------------------------
        n =3
        while n >0:
            
            if start == "Y":

                try: # Does the account excist
                    while n == 3:
                        print("OK lets Log into your Dope A F bank account \n")
                        break
                    name = input("Please enter your user name ")
                    pin = int(input("Please enter your pin "))
#------------------- Getting user information in files ---------------------------------------------                    
                    fpin = open(f"{name}.txt", "r", encoding="utf-8").read().split()
                    print(f"Password = {fpin[5]}\nName = {fpin[2]}")
                    record_name = fpin[2]
                    record_pin = int(fpin[5])
                    os.system("cls")
#------------------ comparing user information with input -----------------------------------------------------------------
                    if name == record_name and pin == record_pin:
                        print(f"Welcome to your Dope A F account {name.capitalize()}")
                        first=input("Would you like to do. Enter C for check balance, D to deposit, W to withdraw and H for transaction history, ").capitalize()
                        if first == "C":
                            account(name)
                        break  
                except: # Start again
                    print("The account is not recognised. Try registering for an account")
                    main()
            
            else:
                n-=1  # Atempts
                print(f"wrong credential {n} more atempts left.")
               
#------------------- Write information to a text file ------------------------------------------------------
        customer_file(name, pin)

        break
    
#------------------- Bank acount information -------------------------------------------------
def account(name):
   
    print("welcome to your account you have £100")
    blank = open(f"{name}.txt","r", encoding="utf-8").read()
    
    #transactions
    print(blank)
    option = input("Type W if you want to withdraw money or type D to deposite money").lower() #withdraw or deposit
    
#---------------------------- Withdrawal ----------------------------------------------------------
    if option == "w":
        figure = float(input("how much would you like to withdraw?"))

#------------------- Text file created for new customer ---------------------------------------------
def customer_file(inname, inpin):
    file_name= f"{inname}.txt"
    open(file_name, "w", encoding="utf-8").write(f"Name = {inname}\nPin = {inpin}\nOverdraft = X\nTotal = Y\nTransactions = Z")
    
         
main()

####################################################################fv