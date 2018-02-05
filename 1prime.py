
import time
start_time = time.time()
upper = 20000

for num1 in range(2,upper):
    for i in range(2,num1):
        if (num1 % i) == 0:
            break
    else:
        print(num1)

print("--- %s seconds ---" % (time.time() - start_time))

"""
import math
import time
start_time = time.time()
upper1 = 20000

for num2 in range(2,upper1):
    for i in range(2,int(math.sqrt(num2))+1):

        if (num2 % i) == 0:
            break
    else:
        print(num2)

print("--- %s seconds ---" % (time.time() - start_time))
"""
