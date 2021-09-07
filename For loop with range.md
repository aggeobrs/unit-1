![1](https://user-images.githubusercontent.com/89012983/132348885-a707ba96-bcab-43c9-b79c-05d42b2220b5.png)

```.py
A=int(input("Enter a number"))
B=int(input("Enter a number"))
for i in range(A, B +1):
    print(i)
```

![2](https://user-images.githubusercontent.com/89012983/132348879-062919db-7ef2-444c-ab4b-39cbf62000ff.png)

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


![3](https://user-images.githubusercontent.com/89012983/132348874-a534d069-20d8-4a7d-9d50-eaace6014876.png)

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


![4](https://user-images.githubusercontent.com/89012983/132348868-1dbfe20e-763f-4209-a43e-8c11989e31b8.png)

```.py
N=int(input("Enter N: "))
S=0
for i in range(N):
    a=int(input("Enter a number: "))
    S=S+a
print(S)
```


![5](https://user-images.githubusercontent.com/89012983/132348860-6efc293e-2b0a-4ff0-8170-b041110ff7e2.png)

```.py
N=int(input("Enter N: "))
S=0
for i in range(N+1):
    S=S+i**3
print(S)
```


![6](https://user-images.githubusercontent.com/89012983/132348856-9d6c14aa-27e3-4d83-b9e5-de05e1ea1659.png)

```.py
N=int(input("Enter N: "))
P=1
for i in range(1,N+1):
    P=P*i
print(P)
```


![7](https://user-images.githubusercontent.com/89012983/132348900-164ced20-241e-4a70-918f-63a4141ed73e.png)

```.py
N=int(input("Enter N: "))
S=0
for i in range(N):
    a=int(input("Enter a number: "))
    if a==0:
        S+=1
print(S)
```


![8](https://user-images.githubusercontent.com/89012983/132348895-54c6bc07-fa0e-4acf-bf7b-6eef58e39b3f.png)

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


![9](https://user-images.githubusercontent.com/89012983/132348888-6c518e50-af8b-446c-b3ce-d485bac67e32.png)

```.py
n=int(input("Enter n: "))
for i in range(1,n+1):
    for y in range(1,i+1):
        print(y, end='')
    print()
```


![10](https://user-images.githubusercontent.com/89012983/132348698-4513bb49-856d-497d-9f14-e62418567661.png)
    
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
