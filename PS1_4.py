# 加载random
import random

# 定义函数Least_moves
def Least_moves(n):
    # 设定初始值为1
    num = 1
    # 初始步骤为0次
    i = 0 
    # 持续循环
    while True:
        # 若初始值等于输入值
        if (num == n):
            # 结束循环
            break
        else:
            # 初始值double后小于等于输入值，则执行double，并步骤+1
            if num * 2 <= n:
                num = num * 2
                i = i + 1
            # 否则执行add，并步骤+1
            else:
                num = num + 1
                i = i + 1
    return i

x = round(random.random()*100)
print()
ans = Least_moves(x)
print("When the random integer x is: ",x,", the smallest number of moves is: ",ans,sep="")