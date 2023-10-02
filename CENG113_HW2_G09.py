#Damla Keleş - 280201057
#Nurcan Yıldız - 280201082
#Group09 - CENG113 
option=0
base=0
decision=0
print("Welcome to Full Adder!")
while decision==0:                 #"Decision" is for the code doesn't stop until the user finishes it. As long as the "decision" is 0, the code continues to ask for "option".
    option = int(input("(1)Compute and Display the Outputs \n(2)Quit \nYou choose: "))    #This line is to ask the user for the option.
    if option !=2 and option != 1:                                          #If the user enters another number instead of 1 or 2,the code prints an error message.
        print("You entered invalid value! Please try again!")
    else:                                                             
        print("You have chosen option", option)                             #If the user enters a valid number, the code print this line.

    while option == 1:
        base = int(input("Which base will you use to enter data lines (base 16/8/2)?: "))    #This line is to ask the user for the base.
        if base==2 or base==8 or base==16:
            while base == 2:                                    #If base is equal to 2 this part will be executed.
                print("You have chosen Binary.")               #Prints the chosen base.
                num = input("Please enter the number: ")        #Asks to the user for the desired number.
                if num == "000" :
                    print("Sum = 0", "\nC_out = 0")
                elif num == "001":
                    print("Sum = 1", "\nC_out = 0")
                elif num == "010":
                    print("Sum = 1", "\nC_out = 0")
                elif num == "011":
                    print("Sum = 0", "\nC_out = 1")
                elif num == "100":
                    print("Sum = 1", "\nC_out = 0")
                elif num == "101":
                    print("Sum = 0", "\nC_out = 1")
                elif num == "110":
                    print("Sum = 0", "\nC_out = 1")
                elif num == "111":
                    print("Sum = 1", "\nC_out = 1")
                else:                                           #If the user enters a number greater than 7 or an invalid number, this error is executed.
                    print("Binary", num, "cannot be represented with 3 bits! Please try again!")
                base=0                                       #Resets the base after the desired number is executed.
            option=0                                      #Resets the option after the desired number is executed.
            
            while base == 8:                                            #If base is equal to 8 this part will be executed.
                print("You have chosen Octal base 8.")
                num = input("Please enter the number: ")
                if num == '0':
                    print("Sum = 0", "\nC_out = 0")
                elif num == '1':
                    print("Sum = 1", "\nC_out = 0")
                elif num == '2':
                    print("Sum = 1", "\nC_out = 0")
                elif num == '3':
                    print("Sum = 0", "\nC_out = 1")
                elif num == '4':
                    print("Sum = 1", "\nC_out = 0")
                elif num == '5':
                    print("Sum = 0", "\nC_out = 1")
                elif num == '6':
                    print("Sum = 0", "\nC_out = 1")
                elif num == '7':
                    print("Sum = 1", "\nC_out = 1")
                else:                                    #If the user enters a number greater than 7 or an invalid number, this error is executed.
                    print("Octal", num, "cannot be represented with 3 bits! Please try again!")
                base=0             
            option=0

            while base == 16:                                          #If base is equal to 8 this part will be executed.
                print("You have chosen hex.")
                num = input("Please enter the number: ")
                if num == '0':
                    print("Sum = 0", "\nC_out = 0")
                elif num == '1':
                    print("Sum = 1", "\nC_out = 0")
                elif num == '2':
                    print("Sum = 1", "\nC_out = 0")
                elif num == '3':
                    print("Sum = 0", "\nC_out = 1")
                elif num == '4':
                    print("Sum = 1", "\nC_out = 0")
                elif num == '5':                            
                    print("Sum = 0", "\nC_out = 1")
                elif num == '6':
                    print("Sum = 0", "\nC_out = 1")
                elif num == '7': 
                    print("Sum = 1", "\nC_out = 1")
                else:                                           #If the user enters a number greater than 7 on base 10 or an invalid number, this error is executed.
                    print("Hex",num, "cannot be represented with 3 bits! Please try again!")
                base=0
            option=0
        
        else:                            #If base is invalid, this error is executed.
            print("You entered invalid base number! Please try again!")
            option=1               #If the base is invalid, the code do not ask again the option thanks to this line. The user has already chosen it.
        option=0 
        
    if option == 2:                              #This part is to stop executing code.
        print("Byee!")
        decision=1                             #We set the decision to 1 so that the code stops asking option when option is 2.