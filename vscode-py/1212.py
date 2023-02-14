import random

# 初始化资金
init_fund = 100
current_fund = init_fund

# 设置运营次数
num_of_rounds = 10

# 首次投注金额为1元
bet_amount = 1

for i in range(num_of_rounds):
    # 抛硬币，0代表正面，1代表反面
    result = random.randint(0, 1)

    if result == 0:
        # 猜对，下次金额为前一次金额-1元，最低不低于1元
        bet_amount = max(bet_amount - 1, 1)
        current_fund += bet_amount
        print(f"第{i+1}次投注：猜对了，赚了{bet_amount}元，剩余资金{current_fund}元。")
    else:
        # 猜错，下次金额为前一次金额+1元
        bet_amount += 1
        current_fund -= bet_amount
        print(f"第{i+1}次投注：猜错了，亏了{bet_amount}元，剩余资金{current_fund}元。")

    # 如果资金不足，退出循环
    if current_fund <= 0:
        print("资金不足，退出投注。")
        break

# 输出最终剩余资金
print(f"最终剩余资金：{current_fund}元。")
