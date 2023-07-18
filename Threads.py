import threading
import time

def longSquare(num):
    time.sleep(1)
    return num**2

def longSquare2(num,results):
    time.sleep(1)
    results[num] = num**2

print('Threads')
a=[longSquare(n) for n in range(0,5)]
print(f'a = {a}')

results = {} #dictionary

t1=threading.Thread(target=longSquare2, args=(1, results))
t2=threading.Thread(target=longSquare2, args=(2, results))

t1.start()
t2.start()

t1.join()
t2.join()

print(f'results = {results}')

#another way to set Threads is by putting them into a list like so
results2 = {}
myThreads = [threading.Thread(target=longSquare2, args=(n, results2)) for n in range(0,10)]
[td.start() for td in myThreads]
[td.join() for td in myThreads]
#In this example we have created 10 threads
print(f'results2 = {results2}')

#Now lets create 100 threads and see what will happen
results3 = {}
myThreads2 = [threading.Thread(target=longSquare2, args=(n, results3)) for n in range(0,100)]
[ta.start() for ta in myThreads2]
[ta.join() for ta in myThreads2]
#In this example we have created 10 threads
print(f'results3 = {results3}')

