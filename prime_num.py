def prime(num):
    for i in range(num+1):
        if i>1:
            for j in range(2,i):
                if i%j==0:
                    break
                else:
                    print(i)
                break
print(prime(6))