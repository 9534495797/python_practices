# x=int(input("your value= "))
# if x%2==0:
#     print("even")
# else:
#     print("odd")


# a=int(input())
# b=int(input())
# c=int(input())
# if a>b and a>c:
#     print("a is largest")
# elif b>a and b>c:
#     print("b is largest")
# else:
#     print("c is largest")


x=int(input("year= "))
if x%4==0:
    if x%100==0:
        if x%400==0:
            print("leap year")
        else:
            print("no leap year")
    else:
        print("yes leap year")
else:
    print("no its not leap year")

    
