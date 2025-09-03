#!/usr/bin/env python3
"""
因子（Factor）概念演示
"""

def find_factors(n):
    """找出数字 n 的所有因子"""
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:  # 如果 n 能被 i 整除（余数为0）
            factors.append(i)
    return factors

def is_factor(n, f):
    """检查 f 是否是 n 的因子"""
    return n % f == 0

def factor_pairs(n):
    """找出因子对（两个因子相乘等于n）"""
    pairs = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            pairs.append((i, n // i))
    return pairs

def demonstrate_factors():
    print("=== 因子（Factor）概念演示 ===\n")
    
    # 示例1: 12的因子
    print("1. 数字 12 的因子：")
    factors_12 = find_factors(12)
    print(f"   12 的所有因子: {factors_12}")
    
    for f in factors_12:
        print(f"   12 ÷ {f} = {12 // f} (余数: {12 % f})")
    
    print(f"   因子对: {factor_pairs(12)}")
    print()
    
    # 示例2: 2020的因子
    print("2. 数字 2020 的因子：")
    factors_2020 = find_factors(2020)
    print(f"   2020 的所有因子: {factors_2020}")
    print(f"   因子对: {factor_pairs(2020)}")
    print()
    
    # 示例3: 位权重 vs 因子
    print("3. 位权重 vs 因子的区别：")
    print("   位权重 [1000, 100, 10, 1] 用于:")
    print("   2020 = 2×1000 + 0×100 + 2×10 + 0×1")
    
    weights = [1000, 100, 10, 1]
    print(f"   这些权重是否都是2020的因子？")
    for w in weights:
        is_f = is_factor(2020, w)
        print(f"   {w} 是 2020 的因子: {is_f}")
        if is_f:
            print(f"     2020 ÷ {w} = {2020 // w}")
    print()
    
    # 示例4: 什么是质因数分解
    print("4. 质因数分解 (Prime Factorization)：")
    print("   将数字分解为质数因子的乘积")
    
    def prime_factors(n):
        factors = []
        d = 2
        while d * d <= n:
            while n % d == 0:
                factors.append(d)
                n //= d
            d += 1
        if n > 1:
            factors.append(n)
        return factors
    
    pf_12 = prime_factors(12)
    pf_2020 = prime_factors(2020)
    
    print(f"   12 = {' × '.join(map(str, pf_12))} = {eval('*'.join(map(str, pf_12)))}")
    print(f"   2020 = {' × '.join(map(str, pf_2020))} = {eval('*'.join(map(str, pf_2020)))}")

def positional_weights_demo():
    print("\n=== 位权重系统演示 ===\n")
    
    number = 2020
    s = str(number)
    
    print(f"数字: {number}")
    print(f"位数: {s}")
    print()
    
    # 计算位权重
    weights = [10**i for i in range(len(s)-1, -1, -1)]
    
    print("位权重分解:")
    total = 0
    for i, (digit, weight) in enumerate(zip(s, weights)):
        digit_val = int(digit)
        contribution = digit_val * weight
        total += contribution
        print(f"  位置 {i+1}: 数字 {digit} × 权重 {weight} = {contribution}")
    
    print(f"\n重建数字: {' + '.join(f'{int(d)}×{w}' for d, w in zip(s, weights))} = {total}")
    
    print(f"\n验证: {total} == {number} ? {total == number}")

if __name__ == "__main__":
    demonstrate_factors()
    positional_weights_demo()

