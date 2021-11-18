words = ["Hello", "I'm Tiep", "I'm learing Python"]
for w in words:
    print(w)
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]
print(users)
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
print(active_users)