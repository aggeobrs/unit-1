```.py
import random
p= random.sample(range(10,99999999), 10)
i=0
for y in range(len(p)):
  while p[y]>9:
    a=p[y]//10
    b=p[y]%10
    i+=1
    p[y]=a*b
  if i>10:
    print(i)
```
