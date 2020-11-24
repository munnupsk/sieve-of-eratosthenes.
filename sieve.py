


import math
max=1001
primes=[1]*max   #assuming all are prime at first

def findPrimes():
    primes[0]=0 
    primes[1]=0 
     
    i=2
    while i<int(math.sqrt(max-1))+1 :
        if primes[i]:
            for j in range(i+i,max,i):   #make jumps of from i+i of size i
                primes[j]=0 
        
        i+=1
findPrimes()
count=0
for i in range(max):
    if primes[i]:
        print(i,end=" ") #print all prime numbers
        count+=1  # count the prime numbers
        
print()
print(count)
