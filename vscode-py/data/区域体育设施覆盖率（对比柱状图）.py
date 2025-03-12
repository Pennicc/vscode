import matplotlib.pyplot as plt
import numpy as np

# 设置全局字体为幼圆（确保系统中已安装）
plt.rc('font', family='YouYuan')

# 数据准备
regions = ['东部', '中部', '西部']
coverage = [58, 42, 34]
per_capita = [2.5, 1.8, 1.2]  # 人均场地面积(m²)

# 设置条形图的条形宽度
bar_width = 0.5  # 您可以根据需要调整这个值

plt.figure(figsize=(10, 6))
bars = plt.bar(regions, coverage, width=bar_width,  # 在这里指定条形宽度
               color=plt.cm.Blues(np.linspace(0.3, 1, len(regions))))

# 添加双数据标签
for bar, cov, area in zip(bars, coverage, per_capita):
    height = bar.get_height()
    # 为了避免标签重叠，可以动态调整标签的位置
    # 这里我们使用条形高度的某个比例来确定标签的上下位置
    label_offset_top = height * 0.1  # 顶部标签的偏移量
    label_offset_bottom = -height * 0.05  # 底部标签的偏移量（注意是负数，表示向下偏移）
    
    # 添加覆盖率标签
    plt.text(bar.get_x() + bar.get_width()/2, height + label_offset_top,
             f"{cov}%", ha='center', va='bottom')
    
    # 添加人均场地面积标签
    # 为了确保底部标签的可读性，我们可以检查条形的颜色，并据此选择标签颜色
    # 但由于我们已经指定了颜色映射，且颜色较深，白色标签通常足够可见
    plt.text(bar.get_x() + bar.get_width()/2, height + label_offset_bottom,
             f"{area}m²", ha='center', va='top', color='white')

plt.title("东中西部体育设施覆盖率对比 (2023)", pad=20)
plt.ylabel("覆盖率 (%)")
plt.ylim(0, 70)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()