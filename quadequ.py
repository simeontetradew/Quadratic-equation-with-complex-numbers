import math
a = float(input('a: ')) 
b = float(input('b: '))
c = float(input('c: '))
d = b**2 - 4*a*c
if (a == 0): # 'a' cannot be zero as a division by zero is not possible.
    print('a = 0') 
else:
    if (d < 0): # Turns 'd' into an imaginary number when its value is below zero and prints out the solutions as complex numbers.
        d = math.sqrt(-d)
        i = 1j
        d = d*i
        x1 = (-b - d)/2/a
        x2 = (-b + d)/2/a
        print('x1 = '+str(x1)+', x2 = '+str(x2))
    elif (d == 0):
        x1 = -b/2/a
        print('x = '+str(x1))
    else:
        x1 = (-b + math.sqrt(d))/2/a
        x2 = (-b - math.sqrt(d))/2/a
        print('x1 = '+str(x1)+', x2 = '+str(x2))
