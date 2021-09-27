```.py
n=input("Enter a number: ")
p=int(n)
i=0
while p>9:
    a=p//10
    b=p%10
    i+=1
    p=a*b
print(i)
 ```
