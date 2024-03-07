import time

n = 100

#O(1)

def O1():
    time.sleep(0.0005)

#O(n)

def On(n):
    for i in range(n):
        time.sleep(0.0005)

#O(n^2)

def On2(n):
    for i in range(n):
        for j in range(n):
            time.sleep(0.0005)

#O(n^3) (if you’ve enough time)

def On3(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                time.sleep(0.0005)

#O(n^4) (don’t try this)

def On4(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    time.sleep(0.0005)

#O(log(n))

def Ologn(n):
    while n > 1:
        n = n // 2
        time.sleep(0.0005)

#O(nlog(n))

def Onlogn(n):
    for i in range(n):
        Ologn(n)

#comparaison des temps d'execution
time1 = time.time()
O1()
time2 = time.time()

print("O(1) : ", time2 - time1)

time1 = time.time()
On(n)
time2 = time.time()

print("O(n) : ", time2 - time1)

time1 = time.time()
On2(n)
time2 = time.time()

print("O(n^2) : ", time2 - time1)

time1 = time.time()
#On3(n)
time2 = time.time()

print("O(n^3) : ", time2 - time1)

time1 = time.time()
#On4(n)
time2 = time.time()

print("O(n^4) : ", time2 - time1)

time1 = time.time()
Ologn(n)
time2 = time.time()

print("O(log(n)) : ", time2 - time1)

time1 = time.time()
Onlogn(n)
time2 = time.time()

print("O(nlog(n)) : ", time2 - time1)