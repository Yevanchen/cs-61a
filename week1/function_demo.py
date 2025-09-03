def make_counter(start):
    count = start
    print(f"创建计数器，初始值: {count}")
    
    def increment():
        nonlocal count
        count += 1
        print(f"increment 函数被调用，count = {count}")
        return count
    
    print(f"返回 increment 函数对象: {increment}")
    return increment

print("=== 创建 counter1 ===")
counter1 = make_counter(0)

print(f"counter1 是什么？ {counter1}")
print(f"counter1 的类型？ {type(counter1)}")

print("\n=== 调用 counter1() ===")
result = counter1()
print(f"返回值: {result}")



