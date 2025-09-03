def make_counter(start):
    count = start  # 外层数据
    
    def increment():
        # nonlocal 关键字用于在嵌套函数中声明变量不是局部的，而是来自最近的外层作用域（但不是全局作用域）。
        # 这样可以在内层函数中修改外层函数的变量。
        nonlocal count
        count += 1
        return count
    
    return increment  # 返回内层函数

# 创建两个独立的计数器
counter1 = make_counter(0)
counter2 = make_counter(100)

print("Counter1:")
print(counter1())  # 1
print(counter1())  # 2
print(counter1())  # 3

print("\nCounter2:")
print(counter2())  # 101
print(counter2())  # 102

print("\nCounter1 again:")
print(counter1())  # 4 (还记得之前的状态!)
