import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rc('font', family='YouYuan')

# 奥运场馆建设资金来源（堆叠柱状图）
# 数据准备
categories = ['2008夏奥会', '2022冬奥会']
government = [51, 35]  # %
social = [49, 65]  # 确保这里的数据已经定义
others = [0, 0]  # 这部分数据在堆叠图中未使用，但如果需要可以保留

fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.5  # 设置条形宽度
bottom = np.zeros(len(categories))
colors = ['#1f77b4', '#2ca02c']  # 注意：这里只使用两个颜色，因为数据只有两层

# 注意：由于这里是堆叠柱状图，我们应该分别绘制每一层
layers = [(government, '政府投资', colors[0]), (social, '社会资本', colors[1])]
for value, name, color in layers:
    bars = ax.bar(categories, value, bottom=bottom, width=bar_width, color=color, label=name)
    bottom += value
    # 添加数值标签
    for bar, val in zip(bars, value):
        height = bar.get_height()
        y_pos = bar.get_y() + height / 2 if bottom[-1] > height / 2 else bottom[-1]  # 调整标签位置以避免重叠
        ax.text(bar.get_x() + bar.get_width() / 2,
                y_pos,
                f"{val}%",
                fontsize=12,
                ha='center', va='center' if bottom[-1] > height / 2 else 'bottom',  # 根据位置调整垂直对齐
                color='white' if color.startswith('#1f') else 'black',  # 根据条形颜色选择标签颜色以确保对比度
                fontweight='bold')

# 设置图例的字体大小
legend_fontsize = 12  # 例如，12 表示字体大小为12点

# 注意：由于我们在后面使用了 bbox_to_anchor 来定位图例，因此不需要在这里使用 loc 参数来指定位置，
# 或者我们可以将 loc 参数设置为一个与 bbox_to_anchor 兼容的值，如 'upper right'，但之后会被 bbox_to_anchor 覆盖。
# 然而，为了清晰起见，我们在这里仍然保留 loc 参数并注释掉，以表明其通常的用法。
ax.legend(loc='upper right',  # 这将被 bbox_to_anchor 覆盖，但可以保留以供参考
          bbox_to_anchor=(1.12, 1 - 0.7 - 0.05),  # 调整这里的值以定位图例
          fontsize=legend_fontsize,  # 设置字体大小
          handleheight=0.05, handlelength=1.2)  # handleheight 和 handlelength 可以根据需要调整

# 注意：上面的 bbox_to_anchor 计算中，我们直接使用了 0.7 而不是通过 ax.get_window_extent().height * legend_vertical_space，
# 因为在绘图之前我们无法准确获取图表的最终高度。因此，这里我们手动调整 bbox_to_anchor 的值以获得所需的图例位置。

ax.set_title("奥运场馆建设资金来源占比", pad=20)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_ylim(0, 100)  # 设置y轴限制以确保堆叠的顶部不被裁剪
plt.show()