

```.py
A=int(input("Enter a number"))
B=int(input("Enter a number"))
for i in range(A, B +1):
    print(i)
```


```.py
A=int(input("Enter a number"))
B=int(input("Enter a number"))
if A<B:
    for i in range(A, B +1):
        print(i)
else:
    for i in range(A,B-1,-1):
        print(i)
```


```.py
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
c=int(input("Enter a number: "))
d=int(input("Enter a number: "))
e=int(input("Enter a number: "))
f=int(input("Enter a number: "))
g=int(input("Enter a number: "))
h=int(input("Enter a number: "))
i=int(input("Enter a number: "))
j=int(input("Enter a number: "))
print(a+b+c+d+e+f+g+h+i+j)
```

```.py
N=int(input("Enter N: "))
S=0
for i in range(N):
    a=int(input("Enter a number: "))
    S=S+a
print(S)
```

```.py
N=int(input("Enter N: "))
S=0
for i in range(N+1):
    S=S+i**3
print(S)
```

```.py
N=int(input("Enter N: "))
P=1
for i in range(1,N+1):
    P=P*i
print(P)
```


```.py
N=int(input("Enter N: "))
S=0
for i in range(N):
    a=int(input("Enter a number: "))
    if a==0:
        S+=1
print(S)
```


```.py
N=int(input("Enter N: "))
S=0
P=1
for i in range(1,N+1):
    for y in range(1,i+1):
        P=P*y
    S=S+P
    P=1
print(S)
```



```.py
n=int(input("Enter n: "))
for i in range(1,n+1):
    for y in range(1,i+1):
        print(y, end='')
    print()
 ```   
    
```.py    
N=int(input("Enter N: "))
S=0
s=0
for i in range(1,N+1):
    S+=i
    if i<N:
        a=int(input("Enter a number: "))
        s+=a
print(S-s)
```   



