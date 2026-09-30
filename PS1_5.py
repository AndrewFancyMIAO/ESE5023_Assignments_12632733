# 加载plt
import matplotlib.pyplot as plt

### 5.1
# 定义函数Find_expression
def Find_expression(n):
    # 创建方案sol和方案数num
    sol = ""
    num = 0
    # 执行3的八次方次循环
    for q in range(3):
        for w in range(3):
            for e in range(3):
                for r in range(3):
                    for t in range(3):
                        for y in range(3):
                            for u in range(3):
                                for i in range(3):
                                    # 设置1-9每个数中间的插入的符号
                                    insert = [q,w,e,r,t,y,u,i]
                                    # 最终结果初始化
                                    exp = "1"
                                    # 对每个空缺进行循环
                                    for o in range(8):
                                        # 当insert值为0时，视为+
                                        if insert[o] == 0:
                                            exp = exp + "+" + str(o+2)
                                        # 当insert值为1时，视为-
                                        elif insert[o] == 1:
                                            exp = exp + "-" + str(o+2)
                                        # 当insert值为2时，视为相连接
                                        else:
                                            exp = exp + str(o+2)
                                    # 当结果的算数运算等于输入值时，记录结果和方案数
                                    if eval(exp) == n:
                                        sol = sol + exp + " = " + str(n) + "\n"
                                        num = num + 1 
    return sol, num
                                        
# 输出1-100的方案list
for x in range(1,101):
    Solution,number = Find_expression(x)
    print("For integer ",x,", the solutions are:\n",Solution,sep="")

### 5.2
# 初始化最大值和最小值
max_Num = -1
min_Num = 10000
max_int = 0
min_int = 0

# 创建方案数Total_solutions方案列表Solutions
Total_solutions = [0 for j in range(100)]
Solutions = [0 for j in range(100)]

# 计算参数1-100的方案列表和方案数
for p in range(1,101):
    Solutions[p-1],Total_solutions[p-1] = Find_expression(p-1)
    # 判断是否为最多方案数
    if Total_solutions[p-1] > max_Num:
        max_Num = Total_solutions[p-1]
        max_int = p
    # 判断是否为最少方案数
    if Total_solutions[p-1] < min_Num:
        min_Num = Total_solutions[p-1]
        min_int =p
    print("For integer ",p,", The number of the solution is ", Total_solutions[p-1],sep="")

# 打印最少方案数和最多方案数
print("Number",min_int,"yields the minimum of Total_solutions, who has",min_Num,"solutions\n" 
      "Number",max_int,"yields the maximum of Total_solutions, who has",max_Num,"solutions")   

## 绘图
plt.plot(range(1,101),Total_solutions)

# 轴命名
plt.xlabel("Integer",fontname = 'Times New Roman')
plt.ylabel("TotalNumber",fontname = 'Times New Roman')

# 保存图片
plt.savefig(r"D:\SUSTech\1stSemester\Computing_and_Programming_for_Environmental_Research\ESE5023_Assignments_12632733\PS1_5.png",
            dpi = 300,
            bbox_inches="tight")

# 输出图片
plt.show()
