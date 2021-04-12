import numpy as np
import time

number = 1000
list = range(number)
time_in = time.time()
for li in list:
    print(li>500)
time_out = time.time()
print(f'List Time Taken {time_out - time_in}')

np_list = np.array([list])
time_in = time.time()
for li in np_list:
    print(li>500)
time_out = time.time()
print(f'Numpy Time Taken {time_out - time_in}')
