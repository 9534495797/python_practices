def palin(word):
    inverse=word[::-1]
    if inverse==word:
        print("yes")
    else:
        print("no")
word=input()
print(palin(word))