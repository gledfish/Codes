#progress bar

import time

scale = 50

print("执行开始".center(scale//2, '-'))

start = time.perf_counter()

for i in range(scale + 1):

  ratio = (i / scale)

  fastPower = pow(ratio + (1 - ratio) / 2, 8)

  movedBar = '*' * int(scale * fastPower)

  residualBar = '.' * int(scale * (1 - fastPower))

  percentFastPower = fastPower * 100

  dur = time.perf_counter() - start

  print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(percentFastPower,
        movedBar, residualBar, dur), end='')

  #time.sleep(0.1)

print("\n"+"执行结束".center(scale//2, '-'))
