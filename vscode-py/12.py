# 定义一个递归函数，返回第n项斐波那契数
def fib(n):
    if n <= 1: # 基本情况
        return n
    else: # 递归情况
        return fib(n-1) + fib(n-2)

# 获取用户输入的项数
nterms = int(input("你需要输出几项? "))

# 检查输入是否合法
if nterms <= 0:
    print("请输入正整数")
else:
    print("斐波那契数列:")
    for i in range(nterms):
        print(fib(i), end=" ") # 输出每一项，以空格分隔