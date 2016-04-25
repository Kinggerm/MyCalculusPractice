from sympy import *
# from fractions import Fraction

x = Symbol('x')
y = eval(input('Function='))
next_x = float(input('x0='))
iteration = int(input('iterations='))

function_y = lambdify(x, y)
function_y_prime = lambdify(x, y.diff(x))
for i in range(iteration):
    # simplified core equation in Newton's method
    next_x = next_x - function_y(next_x)/function_y_prime(next_x)
print('x'+str(iteration)+'='+str(next_x))  # +'~'+str(Fraction(next_x)))

