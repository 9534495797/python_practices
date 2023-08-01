def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
print(gcd(3,7))


# def gcd(num1, num2):
#     if num2 == 0:
#         return num1
#     else:
#         return gcd(num2, num1 % num2)