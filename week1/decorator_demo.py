#!/usr/bin/env python3
"""
装饰器发明者的痛苦经历演示
"""

print("=== 没有装饰器的痛苦世界 ===")

def calculate_score_ugly(student_id):
    print(f"[日志] 调用 calculate_score，参数: {student_id}")  # 污染业务逻辑
    score = student_id * 10  # 真正的业务逻辑
    print(f"[日志] calculate_score 返回: {score}")
    return score

def update_grade_ugly(grade):
    print(f"[日志] 调用 update_grade，参数: {grade}")  # 重复代码
    new_grade = grade + 5
    print(f"[日志] update_grade 返回: {new_grade}")
    return new_grade

print("调用丑陋的函数:")
calculate_score_ugly(8)
update_grade_ugly(75)

print("\n" + "="*50)
print("=== 装饰器拯救世界！ ===")

# 我发明的装饰器
def add_logging(func):
    """给函数添加日志功能的装饰器"""
    def wrapper(*args, **kwargs):
        print(f"[装饰器日志] 调用 {func.__name__}，参数: {args}")
        result = func(*args, **kwargs)
        print(f"[装饰器日志] {func.__name__} 返回: {result}")
        return result
    return wrapper

@add_logging  # 神奇的一行！
def calculate_score(student_id):
    """纯净的业务逻辑，没有日志污染"""
    return student_id * 10

@add_logging
def update_grade(grade):
    """另一个纯净的业务逻辑"""
    return grade + 5

@add_logging
def get_student_name(student_id):
    """第三个函数，也能享受同样的日志功能"""
    names = {1: "Alice", 2: "Bob", 3: "Charlie"}
    return names.get(student_id, "Unknown")

print("调用装饰器版本:")
calculate_score(8)
update_grade(75)
get_student_name(2)

print("\n=== 装饰器的本质 ===")
print("@add_logging 等价于:")
print("calculate_score = add_logging(calculate_score)")

# 手动演示等价性
def manual_function(x):
    return x * 2

print(f"\n原函数: {manual_function}")
manual_function = add_logging(manual_function)  # 手动装饰
print(f"装饰后: {manual_function}")
print("调用手动装饰的函数:")
manual_function(5)
