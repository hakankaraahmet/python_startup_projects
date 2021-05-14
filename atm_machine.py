print("""
      *******************************
      Welcome to atm machine
      
      Operations;
      1- balance inquiry
      2- invest cash
      3- drawing cash
      
      Please click 'q' to exit machine
      *******************************
      """)
balance = 1000
while True:
    operation = input("Please select an operation")
    if operation == "q":
        print("exiting atm")
        break
    elif operation == "1":
        print("Your balance is {} $ ".format(balance))
    elif operation == "2":
        amount = int(input("How much money do you want to invest ? "))
        balance = balance + amount
        print("Your new balance is {} $".format(balance))
    elif operation == "3":
        amount1 = int(input("How much money do you want to draw? "))
        if amount1 < balance:
            balance = balance - amount1
            print("Your new balance is {} $".format(balance))
        else:
            print("insufficent balance")
            continue     
    else:
        print("invalid operation")            