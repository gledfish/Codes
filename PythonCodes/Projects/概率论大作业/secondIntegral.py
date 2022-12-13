# import sympy
# from sympy.interactive import printing
# printing.init_printing(use_latex="mathjax")


# x = sympy.Symbol("x")
# y = sympy.Symbol("y")
# result = float(sympy.integrate(sympy.cos(x**4) + 3 * y**2, (x, 4, 6), (y, 0, 1)))
# print(float(result))
#2.005055086749674

import numpy
N = 10000
accum = 0
for i in range(N):
    x = numpy.random.uniform(4, 6)
    y = numpy.random.uniform(0, 1)
    accum += numpy.cos(x**4) + 3 * y * y
measure = 2 * 1
result = measure * accum/float(N)

print(result)
#2.0020730369355006
