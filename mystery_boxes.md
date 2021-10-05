```.py
def months(a)
  if a>12 or a<1:
    month= FALSE
  else:
    if a=1,6,7:
      month="J"
    elif a=2:
      month="F"
    elif a=3,5:
      month="M"
    elif a=4,8:
      month="A"
    elif a=9:
      month="S"
    elif a=10:
      month="O"
    elif a=11:
      month="N"
    elif a=12:
      month="D"
  return month
```
```.py
def Ebooks(A,B):
  s=0
  for i in range(len(A)):
    if A[i]=="E":
      s+=1
  for i in range(len(B)):
    if B[i]=="E":
      s+=1
  if s>3:
    return True
  else:
    return False
```
```.py
def factorial(A):
  p=1
  for i in range(A):
    p*=i+1
  return p
```
```.py
def acoijaa(word,N):
    letter=chr(N+96).lower()
    s=0
    for i in range(len(word)):
        if letter==word[i]:
            s+=1
    return s
```
```.py
def division(a,b):
    if a%2==0 and b%2==0:
        d=a/b*10
    else:
        d=a*b
    return d
```
```.py
def shift(word):
    n_word=""
    for i in range(len(word)):
        n_word+=chr(ord(word[i])+1)
    return n_word
```
