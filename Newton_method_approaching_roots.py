from sympy import *
# from fractions import Fraction

x = Symbol('x')
y = eval(input('Function='))
next_x = float(input('x0='))
function_y = lambdify(x, y)
function_y_prime = lambdify(x, y.diff(x))
epsilon = float(input('epsilon is: '))
count = 1
while abs(fuction_y(next_x)) > epsilon and count <= 100:
    next_x = next_x - fuction_y(next_x)/fuction_y_prime(next_x)
    count += 1
print('number of iteration:' + str(count) + ' Estimate:' + str(next_x)) 
