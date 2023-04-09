contin = "y" # to start the while loop
while(contin == "y" ):
    print("welcome to my calculator")
    #get the input from the user
    a = float (input("Enter first number: "))
    b = float (input("Enter second number: "))
    #decide the operation
    operato = input("what do you want to do?: +.-,*,/ ")

    #do math operations

    if operato == "+":
        print(a + b)

    if operato == "-":
        print(a - b)

    if operato == "*":  
        print(a * b)

    if operato == "/":
         print(a / b)

    #check if the user wants to quit 
    contin = input("Do you want to continue?: y/n ")

    print("Thank you for using my calculator")

    stall = input("press any key to exit")

    