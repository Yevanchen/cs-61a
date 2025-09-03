"""
Demonstration of the Golden Ratio's iterative property
The golden ratio can be calculated by repeatedly applying: x → 1 + 1/x
"""

def iterative_golden_ratio(guess, iterations=20):
    """
    通过迭代改进计算黄金比例
    φ = 1 + 1/φ
    """
    x = start_value
    print(f"Starting with: {x}")
    print("Iteration | Value")
    print("-" * 20)
    
    for i in range(iterations):
        x = 1 + 1/x
        # f"{i+1:9} | {x:.10f}" 里的 f 是 f-string（格式化字符串字面量），
        # 允许在字符串中直接嵌入表达式并格式化输出。
        # 例如 {i+1:9} 表示宽度为9的右对齐，{x:.10f} 表示 x 保留10位小数。
        print(f"{i+1:9} | {x:.10f}")
    
    return x

# 精确的黄金比例
# 这是精确的黄金比例，因为黄金比例 φ 满足 φ = 1 + 1/φ
# 解这个方程：φ^2 - φ - 1 = 0，解得 φ = (1 + sqrt(5)) / 2
phi_exact = (1 + 5**0.5) / 2
print(f"Exact golden ratio: {phi_exact:.10f}")
print()

# Try with different starting values
print("=== Starting with 2 ===")
result1 = iterative_golden_ratio(2, 15)

print("\n=== Starting with 0.5 ===")
result2 = iterative_golden_ratio(0.5, 15)

print("\n=== Starting with 10 ===")
result3 = iterative_golden_ratio(10, 15)

print(f"\nAll converge to: {phi_exact:.10f}")


