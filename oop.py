
class rectangle():
    def _init_(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b
a=rectangle()
l=int(input())
b=int(input())
print(a.area(l,b))

# class math():
#     def gcd(self,a,b):
#         if b==0:
#             return a
#         else:
#             return self.gcd(b,a%b)
# n=math()
# a=int(input())
# b=int(input())
# print(n.gcd(a,b))