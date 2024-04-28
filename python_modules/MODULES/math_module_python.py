"""
                MATH MODULE
                -----------
1) abs(value)
2) ceil(value)
3) floor(value)
4) log(value) 
5) log(value,base) 
6) round(value) 
7) sin(value) 
8) cos(value) 
9) tan(value) 
10) sqrt(value)
11) isqrt(value)
12) pow(value) 
13) exp(value) 
14) sum(value)
15) fsum(value)
16) degrees(value)
17) radians(value)
18) e 
19) pi 
20) tau
"""
from math import *
#import  math

# 1) abs -> convert negative to positive.
print(f" abs is : {abs(-21.22)},{ abs(10)},{abs(-21)}")

# 2) ceil() -> nearest sabse bada integer .
print(f"ceil is {ceil(5.6)}")

# 3) floor() -> nerest sabse chota integer.
print(f"floor is : {floor(5.99)}")

# 4) log() => find the log .
print(f" log of 25 is {log(25)}")

# 5) log(value,base) => find the log with given base.
print(f"log of 25 with base 2 is {log(25,2)}")

# 6) round(value) => round to the nearest integer.
print(f"round of 25.6 is: {round(25.6)}, 25.7: {round(25.7)}, 25.3: {round(25.3)}, 25.4: {round(25.4)} , 25.5: {round(25.5)} , 25.9: {round(25.9)}")

# 7) sin(value) , 8)cos(value) , 9) tan(value) , :
print(f" sin of 45 is {sin(45)}, cos 80: {cos(80)}, tan29: {tan(29)}")

# 10) sqrt => finding square root & return float value.
print(f" squrae root of 25 : {sqrt(25)}")

# 11) isqrt => return a integer value .
print(f"isqrt of 91 : {isqrt(91)}")

# 12) pow(value,power):
print(f" 2 ki power 5 is : {pow(2,3)}")

# 13) exp(value) -> exp stands for exponential value .
print(f"exponential value of 45 is {exp(45)}")

# 14) sum(value) = l[12,3,4,5,6] works on all iterable
print((f"sum of elemennts in list is {sum([1,2,3,4,5,6,7,8,9,10])}"))

# 15) fsum(value) returns ans in floating point
print(f" sum of elemt : {fsum([1,2,3,4,5])}")

# 16) degree(value) -> convert our value(radian) into degree.
print(f"degree of 45 is : {degrees(45)}")

# 17) radians(degree) =: convert degree to radian .
print(f" radian of degree 25 is {radians(25)}")

#e = 7
# 18) e, pi ;
print(f" e : {e}")

# 19) pi :
print(f"pi : {pi}")

# tau:
print(f" tau: {tau} ")
