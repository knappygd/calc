import math, time, os
from help import help, CORE_SLC, C1_SLC, C2_SLC, C3_SLC

# Console clear
clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

# Help for Core
def core_help():
    print(CORE_SLC)
    showFullHelp = input("Show full help panel? [y/N]: ")
    if showFullHelp == 'y':
        print(help)
    elif showFullHelp == 'N':
        yN_returnFromHelpToM()
        

# Help for Choice 1 
def c1_help():
    print(C1_SLC)
    showFullHelp = input("Show full help panel? [y/N]: ")
    if showFullHelp == 'y':
        print(help)
    elif showFullHelp == 'N':
        yN_returnFromHelpToC1()

# Help for Choice 2
def c2_help():
    print(C2_SLC)
    showFullHelp = input("Show full help panel? [y/N]: ")
    if showFullHelp == 'y':
        print(help)
    elif showFullHelp == 'N':
        yN_returnFromHelpToC2()

# help for Choice 3
def c3_help():
    print(C3_SLC)
    showFullHelp = input("Show full help panel? [y/N]: ")
    if showFullHelp == 'y':
        print(help)
    elif showFullHelp == 'N':
        yN_returnFromHelpToC3()

# invHandler (Invalid inout handler for main_menu())
def invHandler():
    
    print("Input not valid. Check out \x1B[3mhelp\x1B[0m ? [y/N]: ")
    
    invOnMain = input()
        
    if invOnMain == 'y':
        print(help)
    elif invOnMain == 'N':
        main_menu()
    elif invOnMain == 'h':
        print(help)
    elif invOnMain == 'x':
        terminate()
    else:
        invHandler()


# Choice 1            
def choice1():
    
    def recalc_c1():
        time.sleep(1)
        anotherCalc = input("Calculate again? [y/N]: ")
        if anotherCalc == 'y':
            clear()
            choice1()
        elif anotherCalc == 'N':
            terminate()
        elif anotherCalc == 'x':
            terminate()
        elif anotherCalc == 'h':
            clear()
            c1_help()
            recalc_c1()
        else:
            print("Invalid input.")
            quit()
    
    def sum():
        print(f"The result is {fstNum + secNum}")
        time.sleep(1)
        recalc_c1()
            
    def rest():
        print(f"The result is {fstNum - secNum}")
        recalc_c1()
        
    def mul():
        print(f"The result is {fstNum * secNum}")
        recalc_c1()
        
    def div():
            print(f"The result is {fstNum / secNum}")
            recalc_c1()
        
    def flDiv():
        print(f"The result is {fstNum // secNum}")
        recalc_c1()
        
            
    fstNum = float(input("Enter a number: "))
    op = input("Enter an operator: ")
    secNum = float(input("Enter another number: "))
    
    if op == '+':
        sum()
    elif op == '-':
        rest()
    elif op == '*':
        mul()
    elif op == '/':
        div()
    elif op == '//':
        flDiv()
    

# Choice 2                  
def choice2():
    
    def recalc_c2():
        time.sleep(1)
        anotherCalc = input("Calculate again? [y/N]: ")
        if anotherCalc == 'y':
            clear()
            choice2()
        elif anotherCalc == 'N':
            terminate()
        elif anotherCalc == 'x':
            terminate()
        elif anotherCalc == 'h':
            clear()
            c2_help()
            recalc_c2()
        elif anotherCalc == 'r':
            choice2()
        else:
            print("Invalid input.")
            quit()
        
    def sqrt():
        print(f"The square root of {sqrtNum} is {math.sqrt(sqrtNum)}.")
        
    def log():
        print(f"The logarithm of {argNum} in base {log_baseNum} is {math.log(argNum, log_baseNum)}.")
    
    def exp():
        print(f"The result is {exp_baseNum ** expNum}")
            
    print("Do you want to:\n 1. Calculate the square root of a number\n 2. Calculate a power\n 3. Calculate a logarithm\n")
    c2input = input("Enter an option: ")
    
    if c2input == '1':
        sqrtNum = float(input("Enter a number: "))
        sqrt()
        recalc_c2()
    elif c2input == '2':
        exp_baseNum = float(input("Enter the base: "))
        expNum = float(input("Enter the exponent: "))
        exp()
        recalc_c2()
    elif c2input == '3':
        argNum = float(input("Enter the argument: "))
        log_baseNum = float(input("Enter the base: "))
        log()
        recalc_c2()
        
        
    # Core input handlers
    elif c2input == 'x':
        terminate()
    elif c2input == 'h':
        print(help)
    elif c2input == 'r':
        choice2()
        
    # Invalid input handler
    else:
        print("Input not valid. Open the help panel? [y/N]: ")
        invHandler_c2 = input()
        
        if invHandler_c2 == 'y':
            print(help)
            time.sleep(1)
            choice2()
        elif invHandler_c2 == 'N':
            choice2()
        elif invHandler_c2 == 'x':
            terminate()
        elif invHandler == 'r':
            choice2()

    
# Return from help panel to Choice 1 panel
def yN_returnFromHelpToC1():
    time.sleep(1)
    print('Return? [y/N]: ')
    choice = input()
    if choice == 'y':
        clear()
        choice1()
    elif choice == 'N':
        terminate()
    else:
        print("Input not valid: ")
        terminate()
        
# Return from help panel to Choice 2 panel
def yN_returnFromHelpToC2():
    time.sleep(1)
    print('Return? [y/N]: ')
    choice = input()
    if choice == 'y':
        clear()
        choice2()
    elif choice == 'N':
        terminate()
    else:
        print("Input not valid: ")
        terminate()
        
# Return from help panel to Choice 3 panel
def yN_returnFromHelpToC3():
    time.sleep(1)
    print('Return? [y/N]: ')
    choice = input()
    if choice == 'y':
        clear()
        choice3()
    elif choice == 'N':
        terminate()
    else:
        print("Input not valid: ")
        terminate()
        
# Return from help panel to main menu panel
def yN_returnFromHelpToM():
    time.sleep(1)
    print('Return? [y/N]: ')
    choice = input()
    if choice == 'y':
        clear()
        main_menu()
    elif choice == 'N':
        terminate()
    else:
        print("Input not valid: ")
        terminate()
            
# Terminate
def terminate():
    print("Thanks for using the calculator!")
    time.sleep(1)
    clear()
    quit()
    
# Choice 3
def choice3():
    
    def recalc_c3():
        time.sleep(1)
        anotherCalc = input("Calculate again? [y/N]: ")
        if anotherCalc == 'y':
            clear()
            choice3()
        elif anotherCalc == 'N':
            terminate()
        elif anotherCalc == 'x':
            terminate()
        elif anotherCalc == 'h':
            clear()
            c3_help()
            recalc_c3()
        elif anotherCalc == 'r':
            clear()
            choice2()
        else:
            print("Invalid input.")
            quit()
    
    def perc():
        if fstNum > 100:
            print(f"The first number must be 100 or less (your number is {fstNum}).")
            time.sleep(1)
            choice3()
        elif fstNum < 0:
            print(f"The first number must be 0 or greater (your number is {fstNum}).")
            time.sleep(1)
            choice3()
        elif fstNum <= 100 and fstNum >= 0:
            print(f"{fstNum}% of {secNum} is {(fstNum / 100) * secNum}.")
            recalc_c3()
        
    def perc_in():
        if fstNum > secNum:
            print(f"{fstNum} is greater than {secNum}.")
            time.sleep(1)
            choice3()
        elif fstNum < 0:
            print(f"{fstNum} is lesser than 0.")
            time.sleep(1)
            choice3()
        else:
            print(f"{fstNum} represents the {(fstNum * 100) / secNum}% of {secNum}.")
            recalc_c3()
        
    def inc():
        if secNum < fstNum:
            print(f"{secNum} is lesser than {fstNum}.")
            time.sleep(1)
            choice3()
        elif secNum == fstNum:
            print(f"{fstNum} has had no increase.")
            recalc_c3()
        else:
            print(f"{fstNum} has had an increase of {((secNum * 100) / fstNum) / 2}%.")
            recalc_c3()
            
    fstNum = float(input("Enter a number: "))
    op = input("Enter an operator: ")
    secNum = float(input("Enter another number: "))
    
    if op == '%':
        perc()
    elif op == 'in':
        perc_in()
    elif op == 'inc':
        inc()
    elif op == '+':
        opPlusFromC1 = input("'+' is not a valid operator in this instance. Would you like to perform a Choice 1 operation? [y/N]: ")
        if opPlusFromC1 == 'y':
            clear()
            choice1()
        elif opPlusFromC1 == 'N':
            clear()
            choice3()
    elif op == '-':
        opMinFromC1 = input("'-' is not a valid operator in this instance. Would you like to perform a Choice 1 operation? [y/N]: ")
        if opMinFromC1 == 'y':
            clear()
            choice1()
        elif opMinFromC1 == 'N':
            clear()
            choice3()
    elif op == '*':
        opMulFromC1 = input("'*' is not a valid operator in this instance. Would you like to perform a Choice 1 operation? [y/N]: ")
        if opMulFromC1 == 'y':
            clear()
            choice1()
        elif opMulFromC1 == 'N':
            clear()
            choice3()
    elif op == '/':
        opDivFromC1 = input("'/' is not a valid operator in this instance. Would you like to perform a Choice 1 operation? [y/N]: ")
        if opDivFromC1 == 'y':
            clear()
            choice1()
        elif opDivFromC1 == 'N':
            clear()
            choice3()
    elif op == '//':
        opFlDivFromC1 = input("'//' is not a valid operator in this instance. Would you like to perform a Choice 1 operation? [y/N]: ")
        if opFlDivFromC1 == 'y':
            clear()
            choice1()
        elif opFlDivFromC1 == 'N':
            clear()
            choice3()
    else:
        print(f"'{op}' is not a valid operator. Would you like to:\n 1. Try again\n 2. Read \x1B[3mhelp\x1B[0m for more info")
        exChoice = input("Choose: ")
        if exChoice == '2':
            c3_help()
            ret = input()
            if ret == 'x':
                terminate()
            elif ret == 'r':
                choice3()
        elif exChoice == '1':
            choice3()
            
# Main menu            
def main_menu():
    print("What do you want to do?\n 1. Simple math\n 2. Powers, logarithms and square roots\n 3. Percentages\n")
    choice = input("Choose: ")
    
    if choice == '1':
        clear()
        choice1()
    elif choice == '2':
        clear()
        choice2()
    elif choice == '3':
        clear()
        choice3()
    elif choice == 'h':
        clear()
        core_help()
    elif choice == 'x':
        terminate()
    else:
        invHandler()
main_menu()