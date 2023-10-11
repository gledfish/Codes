
from scipy import integrate
import scipy
def f(z, y, x): 
    return scipy.sin(z) + x + scipy.exp(y)

result1 = integrate.tplquad(f, -2, 2, lambda x: (-1) *
                            scipy.sqrt(4 - x * x), lambda x: scipy.sqrt(4 - x * x), 0, lambda x, y: 8 - x * x - y * y)
print(result1)
(121.66509988033158, 7.739990467710454e-07)

import numpy
N = 10000000
accum = 0
z_sum = 0
y_sum = 0
for i in range(N):
    x = numpy.random.uniform(-2, 2)
    y_max = numpy.sqrt(4 - x * x)
    y_min = (-1) * y_max
    y_sum += y_max
    y = numpy.random.uniform(y_min, y_max)
    z_max = 8 - x * x - y * y
    z_sum += z_max
    z = numpy.random.uniform(0, z_max)
    accum += numpy.sin(z) + x + numpy.exp(y)
z_mean = z_sum / N
y_mean = y_sum / N
measure = (2 - (-2)) * 2 * y_mean * (z_mean-0)
result2 =  measure * accum/float(N)


# # print(float(result1))
print(result2)
rate = numpy.abs(result1 - result2) / result1
print(rate)
# print('%.3f%%' % (rate * 100))
# # # 142.49685479297366

