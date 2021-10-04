# Generate Fibonacci Series: {1,1,2,3,5,8,13,21,34,55,89....} using list

#from datetime import datetime
#from time import strftime
import time

"""def gen_fibonacci_1(limit=10):
    Fib_Ser = []
    Fib_Ser.append(1)
    Fib_Ser.append(1)
    for i in range(1,limit-1):
        Fib_Ser.append(Fib_Ser[i-1] + Fib_Ser[i])
        #print(Fib_Ser[i-1])
    return Fib_Ser

limit = 10

#start_time1 = (datetime.now().strftime("%f"))
start_time1 = time.time()
print("\n",gen_fibonacci_1(limit))
#end_time1 = (datetime.now().strftime("%f"))
end_time1 = time.time()
#print(f"Time taken was: {int(end_time1) - int(start_time1)} microseconds")
print(f"Time taken was: {end_time1 - start_time1}")

# Generate Fibonacci Series: {1,1,2,3,5,8,13,21,34,55,89....} using tuples
def gen_fibonacci_2(limit=10):
    num1 = 1
    num2 = 1
    for i in range(limit):
        print(num1)
        (num1,num2) = (num2,num1+num2)

#start_time2 = (datetime.now().strftime("%f"))
start_time2 = time.time()
print(gen_fibonacci_2(limit))
#end_time2 = (datetime.now().strftime("%f"))
end_time2 = time.time()
#print(f"Time taken was: {int(end_time2) - int(start_time2)} microseconds")
print(f"Time taken was: {end_time2 - start_time2}")

# Generate Fibonacci Series: {1,1,2,3,5,8,13,21,34,55,89....} using 'yield' generator
def gen_fibonacci_3(limit=10):
    num1 = 1
    num2 = 1
    for i in range(limit):
        yield num1
        (num1,num2) = (num2,num1+num2)

#start_time3 = (datetime.now().strftime("%f"))
start_time3 = time.time()
for i in gen_fibonacci_3(limit):
    print(i)
#end_time3 = (datetime.now().strftime("%f"))
end_time3 = time.time()
#print(f"Time taken was: {int(end_time3) - int(start_time3)} microseconds")
print(f"Time taken was: {end_time3 - start_time3}")"""

import timeit

stmt1 = '''
gen_fibonacci_1(100)
'''

setup1 = '''
def gen_fibonacci_1(limit=10):
    Fib_Ser = []
    Fib_Ser.append(1)
    Fib_Ser.append(1)
    for i in range(1,limit-1):
        Fib_Ser.append(Fib_Ser[i-1] + Fib_Ser[i])
        #print(Fib_Ser[i-1])
    return Fib_Ser
'''

print(f"Elapsed time of function 1: {timeit.timeit(stmt1,setup1,number=1000000)}")

stmt2 = '''
gen_fibonacci_2(100)
'''

setup2 = '''
def gen_fibonacci_2(limit=10):
    num1 = 1
    num2 = 1
    for i in range(limit):
        #print(num1)
        (num1,num2) = (num2,num1+num2)
'''

print(f"Elapsed time of function 2: {timeit.timeit(stmt2,setup2,number=1000000)}")


stmt3 = '''
gen_fibonacci_3(1000)
'''

setup3 = '''
def gen_fibonacci_3(limit=10):
    num1 = 1
    num2 = 1
    for i in range(limit):
        yield num1
        (num1,num2) = (num2,num1+num2)
'''
print(f"Elapsed time of function 3: {timeit.timeit(stmt3,setup3,number=1000000)}")