from sympy import *

x = Symbol('x')
y = eval(input('Function='))
x_range = [float(k.strip()) for k in input('x1, x2=').split(',')]
position = {'left': 0, 'mean': 0.5, 'right': 1}[input('position(left/mean/right)=')]
iteration = int(input('num(rectangles)='))

width = (x_range[1]-x_range[0])/iteration
next_x = x_range[0]+position*width
function_y = lambdify(x, y)
integral = 0
for i in range(iteration):
    integral += width*function_y(next_x)
    next_x += width
print('Riemann sum='+str(integral))

