# def sum_natural(num):
#     if num==0:
#         return 0
#     elif num==1:
#         return 1
#     else:
#         return num+sum_natural(num-1)
# num=int(input())
# print(sum_natural(num))

def sum_natural(a,b):
    for i in range(a,b+1):
        return b+sum_natural(b-1)
a=int(input())
b=int(input())
print(sum_natural(a,b))