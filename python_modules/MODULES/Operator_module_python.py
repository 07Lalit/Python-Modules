"""
                                     OPERATOR MODULE
                                     ---------------
For many mathematical , logical ,relational , bitwise etc

"""
from operator import  *

# 1) add(a,b) =   a+b
print(f"add(a,b): {add(10,24)}")

# 2) sub(a,b) = a-b
print(f"sub(a,b): {sub(10,24)}")

# 3) mul(a,b) = a*b
print(f"mul(a,b): {mul(10,24)}")

# 4) truediv(a,b): a/b
print(f"truediv(a,b): {truediv(10,2)}")

# 5) floordiv(a,b): a//b
print(f"floordiv(a,b): {floordiv(10,7)}")

# 6) pow(a,b): a**b
print(f"pow(a,b): {pow(10,3)}")

# 7) mod(a,b): a%b
print(f"mod(a,b): {mod(10,3)}")

# 8) lt(a,b): a<b
print(f"lt(a,b): {lt(10,3)}")

# 9) gt(a,b): a>b
print(f"gt(a,b): {gt(10,3)}")

# 10) eq(a,b): a==b
print(f"eq(a,b): {eq(10,3)}")

# 11) ge(a,b): a>=b
print(f"ge(a,b): {ge(10,3)}")

# 12) le(a,b): a<=b
print(f"le(a,b): {le(10,3)}")

# 13) ne(a,b): a!=b
print(f"ne(a,b): {ne(10,3)}")

# 14) iadd(a,b): a=a+b
print(f"iadd(a,b): {iadd(10,3)}")

# 15) iconcat('sita','ram'): concatination and assignment
print(f"iconcat(a,b): {iconcat('sita','ram')}")

# 16) isub(a,b): a=a-b
print(f"isub(a,b): {isub(10,3)}")

# 17) imul(a,b): a=a*b
print(f"imul(a,b): {imul(10,3)}")

# 18) itruediv(a,b): a/=b
print(f"itruediv(a,b): {itruediv(10,3)}")

# 19) imod(a,b): a%=b
print(f"imod(a,b): {imod(10,3)}")

# 20) setitem(object,position,value):
l=[1,2,3,4,5]
print(f"setitem(object,pos,value): {setitem(l,3,10)}")
print(l)

