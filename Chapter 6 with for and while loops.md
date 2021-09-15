```.py
N=int(input())
for i in range(1,N+1):
    if i**2<=N:
        print(i**2)
```
```.py
n = int(input())
i = 1
while i ** 2 <= n:
    print(i ** 2)
    i += 1
```





```.py
n=int(input())
for i in range(2,n+1):
    if n%i==0:
        print(i)
        break
```
```.py
n = int(input())
i = 2
while n % i != 0:
    i += 1
print(i)
```





```.py
n=int(input("Enter a number: "))
for x in range(n+1, 1, -1):
    if 2**x<=n:
        print(x)
        print(2**x)
        break
```
```.py
n=int(input("Enter a number: "))
x=n
while 2**x>=n:
    x-=1
else:
    print(x)
    print(2**x)
   
n=int(input())
x=n
```
     
     
     
     
     
        
```.py        
x=int(input())
y=int(input())
days=1
for i in range(y):
    if x>=y:
        print(days)
        break
    x=x*1.1
    days+=1
```  
```.py    
x = int(input())
y = int(input())
i = 1
while x < y:
    x *= 1.1
    i += 1
print(i)
```








```.py
t=0
for i in range(10):
    a=int(input())
    t+=1
    if a==0:
        t-=1
        print(t)
        break
```
```.py        
t = 0
while int(input()) != 0:
    t += 1
print(t)
```






```.py
sum=0
for i in range(20):
    a=int(input())
    sum+=a
    if a==0:
        print(sum)
        break
```
```.py        
sum = 0
element = int(input())
while element != 0:
    sum += element
    element = int(input())
print(sum)        
```





```.py
sum=0
t=0
for i in range(40):
    a=int(input())
    sum+=a
    t=t+1
    if a==0:
        print(sum/(t-1))
        break
``` 
```.py
sum = 0
len = 0
element = int(input())
while element != 0:
    sum += element
    len += 1
    element = int(input())
print(sum / len)
```




```.py
a=int(input())
max=a
for i in range(40):
    a=int(input())
    if max<a and a!=0:
        max=a
    if a==0:
        print(max)
        break
```
```.py  
max = 0
element = -1
while element != 0:
    element = int(input())
    if element > max:
        max = element
print(max)
```





```.py
a=int(input())
max=a
t=1
index=t
for i in range(40):
    a=int(input())
    t+=1
    if max<a and a!=0:
        max=a
        index=t
    if a==0:
        print(index)
        break
```
```.py
max = 0
index_of_max = -1
element = -1
len = 1
while element != 0:
    element = int(input())
    if element > max:
        max = element
        index_of_max = len
    len += 1
print(index_of_max)
```




```.py
t=0
for i in range(200):
    a=int(input())
    if a%2==0 and a!=0:
        t+=1
    if a==0:
        print(t)
        break
```
```.py
num_even = -1
element = -1
while element != 0:
    element = int(input())
    if element % 2 == 0:
        num_even += 1
print(num_even)
```




```.py
t=0
for i in range(200):
    a=int(input())
    if i==0:
        b=a
    if a>b and a!=0:
        t+=1
    if a==0:
        print(t)
        break
    b=a
```
```.py    
    prev = int(input())
answer = 0
while prev != 0:
    next = int(input())
    if next != 0 and prev < next:
        answer += 1
    prev = next
print(answer)
```




```.py
a=int(input())
max=a
for i in range(40):
    a=int(input())
    if i==0:
        if a<max:
            max2=a
        else:
            max2=max
            max=a
    if a>max:
        max2=max
        max=a
    if max>a and a!=0 and max2<a:
        max2=a
    if a==0:
        print(max2)
        break  
```        
```.py   
first_max = int(input())
second_max = int(input())
if first_max < second_max:
    first_max, second_max = second_max, first_max
element = int(input())
while element != 0:
    if element > first_max:
        second_max, first_max = first_max, element
    elif element > second_max:
        second_max = element
    element = int(input())
print(second_max)
```






```.py
a=int(input())
max=a
t=1
for i in range(40):
    a=int(input())
    if max==a and a!=0:
        t+=1
    if a>max:
        t=1
        max=a
    if a==0:
        print(t)
        break
```
```.py
maximum = 0
num_maximal = 0
element = -1
while element != 0:
    element = int(input())
    if element > maximum:
        maximum, num_maximal = element, 1
    elif element == maximum:
        num_maximal += 1        
print(num_maximal)
```





```.py
n=int(input())
b=1
c=0
if n==0:
    print(0)
elif n==1:
    print(1)
else:
    for i in range(2,n+1):
        a=b+c
        c=b
        b=a
    print(a)
```
```.py    
n = int(input())
if n == 0:
    print(0)
else:
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    print(b)
```




```.py    
n=int(input())
b=1
c=0
if n==0:
    print(0)
elif n==1:
    print(1)
else:
    for i in range(2,n+3):
        a=b+c
        c=b
        b=a
        if a==n:    
            print(i)
            break
        if a>n:
            print(-1)
            break
```   
```.py                
a = int(input())
if a == 0:
    print(0)
else:
    fib_prev, fib_next = 0, 1
    n = 1
    while fib_next <= a:
        if fib_next == a:
            print(n)
            break
        fib_prev, fib_next = fib_next, fib_prev + fib_next
        n += 1
    else:
        print(-1)
```

```.py
b=-1
t=0
maxt=t
a=int(input("enter: "))
for i in range(40):
    if a==0:
        break
    else:
        if a==b:
            t+=1
        else:
            b=a
            if t>maxt:
                maxt=t
            t=1
        a=int(input("enter: "))
if t>maxt:
    maxt=t
print(maxt)
```
```.py                
b=-1
t=0
maxt=t
a=int(input("enter: "))
while a!=0:
    if a==b:
        t+=1
    else:
        b=a
        if t>maxt:
            maxt=t
        t=1
    a=int(input("enter: "))
if t>maxt:
    maxt=t
print(maxt)
```



