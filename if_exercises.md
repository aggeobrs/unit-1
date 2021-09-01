![Untitled Document](https://user-images.githubusercontent.com/89012983/131642210-d9005b76-f4dd-4466-b718-d1d1bb95361d.png)


```.py
a=int(input("enter a number: "))
b=int(input("enter a number: "))
if a>b:
    print(b)
else:
    print(a)
```
![Untitled Document (1)](https://user-images.githubusercontent.com/89012983/131647070-079fdfa0-dea3-43c4-9cb7-91daf1f1c48c.png)
```.py
x=int(input("enter a number: "))
if x>0:
    print(1)
elif x<0:
    print(-1)
else:
    print(0)
```
![Untitled Document (2)](https://user-images.githubusercontent.com/89012983/131648430-6591e9d5-ce07-4997-ad24-2d3d125f4b13.png)
```.py
a=int(input("enter a number: "))
b=int(input("enter a number: "))
c=int(input("enter a number: "))
min=a
if b<min:
    min=b
if c<min:
    min=c
print(min)
```
![Untitled Document (3)](https://user-images.githubusercontent.com/89012983/131650006-9d4f94ea-74a6-471d-8c5c-e8214d3990a7.png)

```.py
a=int(input("enter a number: "))
b=int(input("enter a number: "))
c=int(input("enter a number: "))
if a==b and b==c:
    print(3)
elif a==b or b==c or a==c:
    print(2)
else:
    print(0)
```
![Untitled Document (4)](https://user-images.githubusercontent.com/89012983/131650726-f4dab67c-7c0b-4fda-9be2-9d2557f83fea.png)

```.py
a=int(input("enter a number: "))
b=int(input("enter a number: "))
c=int(input("enter a number: "))
d=int(input("enter a number: "))
if a==c or b==d:
    print("YES")
else:
    print("NO") 
```
![Untitled Document (5)](https://user-images.githubusercontent.com/89012983/131651244-61c2ac89-14f4-4233-b9ce-c2995f66c9f2.png)

```.py
a=int(input("enter a number: "))
b=int(input("enter a number: "))
c=int(input("enter a number: "))
d=int(input("enter a number: "))
if (a+b)%2==(c+d)%2:
    print("YES")
else:
    print("NO")
```
![Untitled Document (6)](https://user-images.githubusercontent.com/89012983/131652401-78b1f271-3ddf-4753-bbd4-927088b74f55.png)

```.py
a=int(input("enter a number: "))
b=int(input("enter a number: "))
c=int(input("enter a number: "))
d=int(input("enter a number: "))
if (a==c+1 or a==c or a==c-1) and (b==d or b==d+1 or b==d-1):
    print("YES")
else:
    print("NO")
```
![Untitled Document (7)](https://user-images.githubusercontent.com/89012983/131653004-6391206e-9c32-4eaf-ac7f-6be199e29b78.png)

```.py
a=int(input("enter a number: "))
b=int(input("enter a number: "))
c=int(input("enter a number: "))
d=int(input("enter a number: "))
if abs(a-c)==abs(b-d):
    print("YES")
else:
    print("NO")
```
![Untitled Document (8)](https://user-images.githubusercontent.com/89012983/131653438-5a401310-ff28-4877-afb5-4d540d480447.png)

```.py
a=int(input("enter a number: "))
b=int(input("enter a number: "))
c=int(input("enter a number: "))
d=int(input("enter a number: "))
if abs(a-c)==abs(b-d) or (a==c or b==d):
    print("YES")
else:
    print("NO")
```
 ![Untitled Document (9)](https://user-images.githubusercontent.com/89012983/131658016-f1a1a831-371c-4294-87e4-3aa6f72f1926.png)

```.py
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (d == b + 1 or d == b - 1) and (c == a - 2 or c == a + 2):
  print ("YES")
elif (c == a + 1 or c == a - 1) and (d == b - 2 or d == b + 2):
  print ("YES")
else:
  print ("NO")
```
![Untitled Document (10)](https://user-images.githubusercontent.com/89012983/131658269-742b166a-0757-43ad-b34e-2a3212993ae7.png)

```.py
m=int(input("enter a number: "))
n=int(input("enter a number: "))
k=int(input("enter a number: "))
if (k%n==0 or k%m==0) and k<m*n:
    print("YES")
else:
    print("NO")
```
![Untitled Document (11)](https://user-images.githubusercontent.com/89012983/131658544-d040cb88-9c87-4743-827d-1b16050fcff0.png)

```.py
a=int(input("enter the year: "))
if a%4==0 and a%100!=0 or a%400==0:
    print("LEAP")
else:
    print("COMMON")
```
