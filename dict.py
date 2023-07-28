# user={'name':'ankit','age':20}
# print(user)
# print(type(user))
# print(user['name'])
user={'name':'Ankit','age':'21'}
print(user)
print(type(user))
print(user['name'])
if 'name' in user:
    print("yes")
else:
    print("no")

if 'Ankit' in user.values():
    print("yes")
else:
    print("no")

for i in user:
    print(i)
for i in user.keys():
    print(i)
for i in user.values():
    print(i)



# user_info={
#     'name':'ankit',
#     'age':20,
#     'cast':'brahman',
#     'religious':'hindu',
#     'nation':'hindustan'
# }
# print(user_info )

# if 'name' in user_info:
#     print("yes")
# else:
#     print("no")

# if 20 in user_info.values():
#     print("yes")
# else:
#     print("no")

# for i in user_info:
#     print(i)

# for i in user_info.keys():
#     print(i)
# for i in user_info.values():
#     print(i)