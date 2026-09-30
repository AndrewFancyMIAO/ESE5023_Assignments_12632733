# 先定义一个阶乘函数factorial
def factorial(n):
    res = 1
    for i in range(1, n+1):
        res = res * i
    return res

# 定义函数Pascal_triangle
def Pascal_triangle(k):
    # 创建一个k+1列值为0的数组
    result = [0 for i in range(k+1)]
    for i in range(k+1):
        # 使用formula "k choose in i"计算数值
        result[i] = factorial(k)/(factorial(i)*factorial(k-i))
    return result

# 输出第100行的结果
print("The results of the line 100 are: ")
for number in Pascal_triangle(100):
    print(number)

# 输出第200行的结果
print("The results of the line 200 are: ")
for number in Pascal_triangle(200):
    print(number)
