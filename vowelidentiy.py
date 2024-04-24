# x=str(input("word= "))
# if 'a' in x:
#         print("vowel")
# elif 'e' in x:
#       print("vowel")
# elif 'i' in x:
#       print("vowel")
# elif 'o' in x:
#       print("vowel")
# elif 'u' in x:
#       print("vowel")
# else:
#     print("constant")

x=str(input())
if x=="a" or "e" or "i" or "u" or"o":
    print("vowel")
elif x.isalpha():
    print("consonant")
else:
    print("invalid input")