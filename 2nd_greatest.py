a=int(input())
b=int(input())
c=int(input())
if a>b and a<c or a>c and a<b:
    print("a is 2nd largest")
elif b>a and b<c or b>c and b<a:
    print("b is second largest")
else:
    print("c is 2nd largest")