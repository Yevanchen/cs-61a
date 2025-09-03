# CS61A Lab01 练习问卷

## 第一部分：控制流 (Control Flow)

### 问题1：条件语句分析
给定函数：
```python
def xk(c, d):
    if c == 4:
        return 6
    elif d >= 4:
        return 6 + 7 + c
    else:
        return 25
```

请计算以下函数调用的结果：

1. `xk(10, 10)` = ______
2. `xk(10, 6)` = ______  
3. `xk(4, 6)` = ______
4. `xk(0, 0)` = ______

### 问题2：打印与返回值分析
给定函数：
```python
def how_big(x):
    if x > 10:
        print('huge')
    elif x > 5:
        return 'big'
    elif x > 0:
        print('small')
    else:
        print("nothin")
```

请分析以下函数调用的输出和返回值：

1. `how_big(7)` 输出：______ 返回值：______
2. `how_big(12)` 输出：______ 返回值：______
3. `how_big(1)` 输出：______ 返回值：______
4. `how_big(-1)` 输出：______ 返回值：______

### 问题3：while循环分析

**循环1：**
```python
n = 3
while n >= 0:
    n -= 1
    print(n)
```
输出：
______
______
______
______

**循环2：**
```python
positive = 28
while positive:
    print("positive?")
    positive -= 3
```
这个循环会：______（填写：输出几次"positive?"，或者"无限循环"）

**循环3：**
```python
positive = -9
negative = -12
while negative:
    if positive:
        print(negative)
    positive += 3
    negative += 3
```
输出：
______
______
______

## 第二部分：条件语句进阶 (If Statements)

### 问题4：嵌套条件分析

**函数1：**
```python
def ab(c, d):
    if c > 5:
        print(c)
    elif c > 7:
        print(d)
    print('foo')
```
`ab(10, 20)` 的输出：
______
______

**函数2：**
```python
def bake(cake, make):
   if cake == 0:
       cake = cake + 1
       print(cake)
   if cake == 1:
       print(make)
   else:
       return cake
   return make
```

1. `bake(0, 29)` 输出：______ ______ 返回值：______
2. `bake(1, "mashed potatoes")` 输出：______ 返回值：______

## 第三部分：调试知识 (Debugging Quiz)

### 问题5：错误追踪分析
给定错误追踪：
```
Traceback (most recent call last):
    File "temp.py", line 10, in <module>
      f("hi")
    File "temp.py", line 2, in f
      return g(x + x, x)
    File "temp.py", line 5, in g
      return h(x + y * 5)
    File "temp.py", line 8, in h
      return x + 0
  TypeError: must be str, not int
```

1. 最近的函数调用是：______
   - A) f("hi")
   - B) g(x + x, x)
   - C) h(x + y * 5)

2. 错误的原因是：______
   - A) 代码试图将字符串和整数相加
   - B) 代码进入了无限循环
   - C) 缺少return语句

### 问题6：doctest语法
如何编写一个doctest来断言 `square(2) == 4`？______
- A) `doctest: (2, 4)`
- B) `input: 2 output: 4`
- C) `square(2) 4`
- D) `>>> square(2) 4`

### 问题7：调试最佳实践

1. 什么时候应该使用print语句？______
   - A) 用于永久调试，以便对代码有长期信心
   - B) 确保代码中某些点的某些条件为真
   - C) 调查代码中某些点的变量值

2. 如何防止ok自动评分器将print语句解释为输出？______
   - A) 不需要做任何事，ok只查看返回值，不查看打印值
   - B) 在输出行前面打印'DEBUG:'
   - C) 在输出行前面打印#

3. 调查lab01中sum_digits问题失败测试的最佳方法是什么？______
   - A) `python3 ok -q sum_digits -i`
   - B) `python3 ok -q sum_digits --trace`
   - C) `python3 ok -q sum_digits`
   - D) `python3 -i lab01.py`

4. 查看环境图来调查lab01中sum_digits问题失败测试的最佳方法是什么？______
   - A) `python3 ok -q sum_digits -i`
   - B) `python3 ok -q sum_digits --trace`
   - C) `python3 ok -q sum_digits`
   - D) `python3 -i lab01.py`

### 问题8：错误类型识别

1. 你得到SyntaxError。最可能发生了什么？______
   - A) 括号不匹配
   - B) 缩进混合了制表符和空格
   - C) 忘记了return语句
   - D) 变量名输入错误

2. 你得到IndentationError。最可能发生了什么？______
   - A) 括号不匹配
   - B) 缩进混合了制表符和空格
   - C) 忘记了return语句
   - D) 变量名输入错误

3. 你得到TypeError: ... 'NoneType' object is not ...。最可能发生了什么？______
   - A) 括号不匹配
   - B) 缩进混合了制表符和空格
   - C) 忘记了return语句
   - D) 变量名输入错误

4. 你得到NameError。最可能发生了什么？______
   - A) 括号不匹配
   - B) 缩进混合了制表符和空格
   - C) 忘记了return语句
   - D) 变量名输入错误

### 问题9：编程最佳实践
以下哪个说法是**错误**的？______
- A) 返回错误答案而不是崩溃的代码通常更好，因为它至少工作正常
- B) 测试对于确保健壮的代码非常重要
- C) 调试不能替代测试
- D) 在发布的代码中留下调试打印语句通常是不好的做法
- E) 在发布的代码中留下断言语句通常是好的做法

## 第四部分：编程实现

### 问题10：函数实现
请实现以下三个函数（在lab01.py文件中）：

1. **falling(n, k)** - 计算n的k阶下降阶乘
2. **sum_digits(y)** - 计算数字y的各位数之和
3. **double_eights(n)** - 判断n是否包含连续的两个8

---

## 答题说明
1. 在每个______处填入你的答案
2. 对于选择题，填入选项字母（A、B、C、D、E）
3. 对于计算题，填入具体数值或字符串
4. 对于输出题，按实际输出格式填写
5. 编程题请在对应的.py文件中实现

完成后可以运行 `python3 -m doctest lab01.py -v` 来测试你的实现！

