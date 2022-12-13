# import sympy
# from sympy.interactive import printing
# printing.init_printing(use_latex="mathjax")

# x = sympy.Symbol("x")
# result = sympy.integrate(x**2, (x, 1, 5))
# print(float(result))
# 41.333333333333336

import numpy
N = 100000
accum = 0
for i in range(N):
    x = numpy.random.uniform(1,5)
    accum += x**2
measure = 5 - 1
result = measure * accum / float(N)
print(result)
# 41.38841335712615
