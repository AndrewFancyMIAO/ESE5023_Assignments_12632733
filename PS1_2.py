### 2.1
# 加载random
import random

# 创建一个值为0的5行10列矩阵M1
M1 = [[0 for j in range(10)] for i in range(5)]

# 创建一个值为0的10行5列矩阵M2
M2 = [[0 for j in range(5)] for j in range(10)]

# 为M1赋值
# 循环5行
for i in range(5):
    # 循环10列
    for j in range(10):
        # M1[i][j]的值为0-50的整数
        M1[i][j] = round((random.random()*100)/2)
print("The matrix M1 is: ",M1,"\n")

# 为M2赋值
# 循环10行
for i in range(10):
    # 循环5列
    for j in range(5):
        # M2[i][j]的值为0-50的整数
        M2[i][j] = round((random.random()*100)/2)
print("The matrix M2 is: ",M2,"\n")

### 2.2
# 定义函数Matrix_multip
def Matrix_multip(A,B):
    # 读取矩阵A的行数
    rows = len(A)
    # 读取矩阵B的列数
    cols = len(B[0])
    # 建立结果矩阵
    res = [[0 for j in range(cols)] for i in range(rows)]
    # 计算乘法
    for i in range(rows):
        for j in range(cols):
            for k in range(len(B)):
                res[i][j] = A[i][k] + B[k][j]
    return res

M3 = Matrix_multip(M1, M2)
print("The answer is: ",M3)