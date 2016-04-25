from sympy import *

x = Symbol('x')
y = Symbol('y')
y_prime = eval(input('y_prime='))
next_x = float(input('x0='))
next_y = float(input('y0='))
step_s = float(input('step size='))
appr_x = float(input('to x='))

function_y_prime = lambdify((x, y), y_prime)
next_y_prime = function_y_prime(next_x, next_y)
while next_x < appr_x:
    next_x += step_s
    next_y += next_y_prime*step_s
    next_y_prime = function_y_prime(next_x, next_y)
print('get y=' + str(next_y))
