# 定义函数Print_values
def Print_values():
    # 输入a,b,c
    a = int(input("Please enter a: "))
    b = int(input("Please enter b: "))
    c = int(input("Please enter c: "))
    #判断a，b大小
    if (a > b):
        # 若a > b，则
        # 判断b，c大小
        if (b > c):
            # 若b > c，则
            print(a,b,c)
        else:
            # 若b < c，则
            # 判断a，c大小
            if (a > c):
                # 若a > c，则
                print(a,c,b)
            else:
                # 若a < c，则
                print(c,a,b)        
    else:
        # 若a < b，则
        # 判断b，c大小
        if (b > c):
            # 若b > c，则
            print("No Answer")
        else:
            # 若b < c，则
            print(c,b,a)
    return a,b,c
# 运行Print_values函数            
Print_values()
                
                  