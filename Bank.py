import os
# Welcome message
print("Welcome to Dope A F bank. The home of your banking needs ")

######### Log into your bank########################

# Do you have an account?

start = input("Do you have an account. Please type Y for yes and N for No. ").capitalize().strip()
os.system("cls")
while True:
    # Register
    if start == "N":
        print("A new customer Great. You will not regret joining Dope A F.\n")
        inname = input("What is your user name ")
        inpin = int(input("What is your pin "))
        os.system("cls")
        start="Y"
# login       
    n =3
    while n >0:
        
        if start == "Y":
            while n == 3:
                print("OK lets Log into your Dope A F bank account \n")
                break
            name = input("Please enter your user name ")
            pin = int(input("Please enter your pin "))
            os.system("cls")
        if pin == inpin and name ==inname:
            print(f"Welcome to your Dope A F account {name.capitalize()}")
            break  
        
        else:
            print(f"wrong credential {n} more atempts left.")
            n-=1
    
    print("Would you like to check your balance?")
    break
####################################################################