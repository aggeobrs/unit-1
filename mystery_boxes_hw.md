```.py
def mystery_box1(word, statement):
    n_word=""
    if statement == True:
        n_word=''.join(reversed(word))
        n_word=n_word.lower()
    else:
        n_word=''.join(reversed(word))
    print(n_word)
```    
```.py    
def mystery_box2(email):
    domain = email.split('@')[1]
    full_name = email.split('@')[0]
    name=full_name.split('.')[0]
    surname=full_name.split('.')[1]
    name= name.capitalize() + " " + surname.capitalize()
    print(f"The name is {name} and the domain is {domain}.")
```
```.py
def mystery_box3(a,b,c):
    min=a
    if b<min:
        min=b
    if c<min:
        min=c
    if min==4:
        d=2*a*b*c/(min)
    elif min==4:
        d=a*b*c/(min)/2
    else:
        d=a*b*c/(min)
    print(d)
```
```.py
def mystery_box4(list):
    n_list=[0,0,0,0,0]
    n=0
    s=0
    for i in range(len(list)):
        if list[i]<8:
            n_list[n]+=list[i]
            s+=list[i]
            n+=1
        average=s/n
    print(average, n_list)
```    
