start = input("Do you have an account. Please type Y for yes and N for No. ").capitalize().strip()
while True:
    # Register
    if start == "N":
        print("A new customer Great. You will not regret joining Dope A F.\n")
        inname = input("What is your user name ")
        while True:
            try:
                inpin = int(input("What is your pin "))
                if len(str(inpin)) == 4:
                    break
                else:
                    print("Your pin has to be 4 numbers. It can not have letters. No more and no less")

            except:
                print("Your pin has to be 4 numbers. It can not have letters. No more and no less")
                continue
    print("bye!")
    break

