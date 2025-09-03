

def sum_digits(n):
  if n < 10:
    return n
  else :
    left,right = n//10,n%10
    return sum_digits(left)+right



def product_1_to_n(n):
    """返回1到n的连乘积"""
    if n == 1:
        return 1
    else:
        return n * product_1_to_n(n-1)






print(sum_digits(12345))   # 15
print(sum_digits(0))       # 0
print(sum_digits(9))       # 9
print(sum_digits(1001))    # 2
print(sum_digits(987654321)) # 45
