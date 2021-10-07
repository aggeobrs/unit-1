```.py
def quiz2(A,B,C):
    #find differences
    d1=abs(A-B)
    d2=abs(B-C)
    d3=abs(C-A)
    max=d1
    #find max
    if d2>max:
        max=d2
    if d3>max:
        max=d3
    return max
```
