users = [
    {'name': 'Alice', 'age': 25, 'score': 85},
    {'name': 'Bob', 'age': 30, 'score': 92},
    {'name': 'Charlie', 'age': 22, 'score': 78}
]

def get_age(user):
    return user['age']

# 你传了整个 users 列表进去，get_age 只会取 users[0]['age']
result = get_age(users[0])
print("get_age(users) 返回:", result)
