# -*- coding: utf-8 -*-
"""Quiz#002

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JDHiPxXsaw2VH4awtxulVwH1hmeayZ-C
"""

def largestDistance(A,B,C):
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

print(largestDistance(1, 2, 3))
print(largestDistance(1, 3, 10))
print(largestDistance(3, 2, 4))