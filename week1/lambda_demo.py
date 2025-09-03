# Lambda 基础示例

# 1. 简单的数学运算
square = lambda x: x * x
add = lambda x, y: x + y
multiply_by_2 = lambda x: x * 2

print("=== 基本 Lambda ===")
print(f"square(5) = {square(5)}")
print(f"add(3, 4) = {add(3, 4)}")
print(f"multiply_by_2(7) = {multiply_by_2(7)}")

# 2. 在高阶函数中使用 Lambda
numbers = [1, 2, 3, 4, 5]

print("\n=== 配合 map 使用 ===")
squared_numbers = list(map(lambda x: x**2, numbers))
print(f"原列表: {numbers}")
print(f"平方后: {squared_numbers}")

print("\n=== 配合 filter 使用 ===")
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"原列表: {numbers}")
print(f"偶数: {even_numbers}")

print("\n=== 配合 sorted 使用 ===")
words = ["apple", "pie", "a", "longer"]
sorted_by_length = sorted(words, key=lambda word: len(word))
print(f"原列表: {words}")
print(f"按长度排序: {sorted_by_length}")

# 3. 对比普通函数写法
print("\n=== 对比普通函数 ===")

# 普通函数方式
def get_length(word):
    return len(word)

sorted_normal = sorted(words, key=get_length)
sorted_lambda = sorted(words, key=lambda word: len(word))

print(f"普通函数结果: {sorted_normal}")
print(f"Lambda 结果: {sorted_lambda}")

# 4. 立即调用的 Lambda
print("\n=== 立即调用 Lambda ===")
result = (lambda x, y: x * y + 10)(3, 4)
print(f"(lambda x, y: x * y + 10)(3, 4) = {result}")

# 5. Lambda 的限制 - 只能写表达式，不能写语句
print("\n=== Lambda 限制 ===")
# 这样是可以的
conditional = lambda x: "positive" if x > 0 else "non-positive"
print(f"conditional(5) = {conditional(5)}")
print(f"conditional(-3) = {conditional(-3)}")

# 这样是不行的（不能在 lambda 中使用 print）
# bad_lambda = lambda x: print(x)  # SyntaxError!

# 我有一堆数据要处理
numbers = [1, 5, 3, 8, 2, 9, 4]

# 用 lambda 按照"距离5的远近"排序
sorted_numbers = sorted(numbers, key=lambda x: abs(x - 5))


# 我要对用户数据做各种操作
users = [
    {'name': 'Alice', 'age': 25, 'score': 85},
    {'name': 'Bob', 'age': 30, 'score': 92},
    {'name': 'Charlie', 'age': 22, 'score': 78}
]

# 各种一次性的小函数
def get_age(user):
    return user['age']

def get_score(user):
    return user['score']

def is_adult(user):
    return user['age'] >= 18

def is_high_scorer(user):
    return user['score'] >= 85

# 使用时代码分散，很烦
sorted_by_age = sorted(users, key=get_age)
adults = filter(is_adult, users)
high_scorers = filter(is_high_scorer, users)