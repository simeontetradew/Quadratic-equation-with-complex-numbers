import math
def main():
    print('Quadratic equation is a type of equation where ax^2+bx+c=0, now please type your coefficients below: ') # Prints out a starting message.
def menu(): # This is the main program.
    try:
        a = float(input('a: '))
        zero = 1/a # This is used in order to print out the divide-by-zero-message from the point where the value of 'a' is set to 0.
        b = float(input('b: '))
        c = float(input('c: '))
        d = b**2 - 4*a*c
        if (d < 0):
            def q(a, d): # Asks the user if he wants to use the option to express the solutions (which aren't real) using complex numbers.
                ans = input('The discriminant`s value is below zero, do you want to solve the equation using imaginary numbers? Type "y" for YES and "n" for "NO": ')
                if (ans == 'y'):
                    d = math.sqrt(-d) #
                    i = 1j            # These 3 lines are used in order to convert the square root of 'd' to an imaginary number.
                    d = d*i           #
                    x1 = (-b - d)/2/a
                    x2 = (-b + d)/2/a
                    print('The value of x1 is ' + str(x1) + ', and the value of x2 is ' + str(x2)) # Prints out the values of the 2 solutions using complex numbers.
                elif (ans == 'n'):
                    print('The equation has no real answers.')
                else:
                    print('Invalid option, please choose type "y" or "n": ') # Makes the user choose if he wants to use complex numbers or not.
                    return q(a, d)
            q(a, d)
        elif (d == 0):
            x1 = -b/2/a
            print('The value of x is ' + str(x1)) # Prints out the value of the 1 and only solution.
        else:
            x1 = (-b + math.sqrt(d))/2/a
            x2 = (-b - math.sqrt(d))/2/a
            print('The value of x1 is ' + str(x1) + ', and the value of x2 is ' + str(x2)) # Prints out the values of the 2 solutions. 
    except ZeroDivisionError: # Runs when a value of 0 has been set to 'a'.
        print('The value of "a" cannot be "0" as a division by zero is not possible, please try another value of "a": ') 
        return menu() # Makes the user type another value for 'a' and then type the values for 'b' and 'c'.
    except ValueError: # Runs where a user has typed a string or character instead of number for 'a', 'b' or 'c'.
        print('You must type real numbers in order for the program to work, please try again: ')
        return menu() # Makes the user type another values for the 3 coefficients.
main()
menu()
def cont(): # Prints out so the user can try another equation without running the code again.
    ans = input('You can type "y" in order to try another one, or type "n" to quit: ')
    if (ans == 'y'):
        return menu()+cont() # Prints both the selection of coefficients and the option to solve another equation.
    elif (ans == 'n'):
         quit() # Cancels the code.
    else:
        print('Invalid option, please choose type "y" or "n": ')
        return cont() # Makes the user choose if he wants to continue or cancel the code.
cont()


     
