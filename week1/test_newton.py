#!/usr/bin/env python3
"""
牛顿法测试用例
包含5个不同的测试场景
"""

import math
from Newton import newton_method, sqrt_newton

def test_case_1_quadratic_function():
    """
    测试用例1: 二次函数 f(x) = x^2 - 4
    期望零点: x = 2 或 x = -2
    """
    print("=" * 50)
    print("测试用例1: 求解 x^2 - 4 = 0")
    
    def f(x):
        return x * x - 4
    
    def df(x):
        return 2 * x
    
    # 从正数开始
    root1 = newton_method(f, df, initial_guess=3.0)
    print(f"从初始值3.0开始，找到零点: {root1:.10f}")
    print(f"验证: f({root1:.10f}) = {f(root1):.2e}")
    
    # 从负数开始
    root2 = newton_method(f, df, initial_guess=-3.0)
    print(f"从初始值-3.0开始，找到零点: {root2:.10f}")
    print(f"验证: f({root2:.10f}) = {f(root2):.2e}")

def test_case_2_cubic_function():
    """
    测试用例2: 三次函数 f(x) = x^3 - 2x - 5
    """
    print("=" * 50)
    print("测试用例2: 求解 x^3 - 2x - 5 = 0")
    
    def f(x):
        return x**3 - 2*x - 5
    
    def df(x):
        return 3*x**2 - 2
    
    root = newton_method(f, df, initial_guess=2.0)
    print(f"找到零点: {root:.10f}")
    print(f"验证: f({root:.10f}) = {f(root):.2e}")

def test_case_3_square_root():
    """
    测试用例3: 使用牛顿法计算平方根
    """
    print("=" * 50)
    print("测试用例3: 使用牛顿法计算平方根")
    
    numbers = [4, 9, 16, 25, 2]
    
    for n in numbers:
        calculated_sqrt = sqrt_newton(n)
        actual_sqrt = math.sqrt(n)
        error = abs(calculated_sqrt - actual_sqrt)
        
        print(f"√{n} = {calculated_sqrt:.10f} (实际值: {actual_sqrt:.10f}, 误差: {error:.2e})")

def test_case_4_trigonometric_function():
    """
    测试用例4: 三角函数 f(x) = sin(x) - 0.5
    求解 sin(x) = 0.5
    """
    print("=" * 50)
    print("测试用例4: 求解 sin(x) - 0.5 = 0")
    
    def f(x):
        return math.sin(x) - 0.5
    
    def df(x):
        return math.cos(x)
    
    # 寻找π/6附近的解
    root = newton_method(f, df, initial_guess=0.5)
    print(f"找到零点: {root:.10f}")
    print(f"验证: sin({root:.10f}) = {math.sin(root):.10f}")
    print(f"理论值 π/6 = {math.pi/6:.10f}")
    print(f"误差: {abs(root - math.pi/6):.2e}")

def test_case_5_exponential_function():
    """
    测试用例5: 指数函数 f(x) = e^x - 2
    求解 e^x = 2, 即 x = ln(2)
    """
    print("=" * 50)
    print("测试用例5: 求解 e^x - 2 = 0")
    
    def f(x):
        return math.exp(x) - 2
    
    def df(x):
        return math.exp(x)
    
    root = newton_method(f, df, initial_guess=1.0)
    print(f"找到零点: {root:.10f}")
    print(f"验证: e^{root:.10f} = {math.exp(root):.10f}")
    print(f"理论值 ln(2) = {math.log(2):.10f}")
    print(f"误差: {abs(root - math.log(2)):.2e}")

def run_all_tests():
    """运行所有测试用例"""
    print("牛顿法测试用例集")
    print("=" * 50)
    
    try:
        test_case_1_quadratic_function()
        test_case_2_cubic_function()
        test_case_3_square_root()
        test_case_4_trigonometric_function()
        test_case_5_exponential_function()
        
        print("=" * 50)
        print("所有测试用例执行完成！")
        
    except Exception as e:
        print(f"测试过程中出现错误: {e}")

if __name__ == "__main__":
    run_all_tests()
