import matplotlib.pyplot as plt
import numpy as np

# 设置全局字体为幼圆（确保系统中已安装）
plt.rc('font', family='YouYuan')

# 冰雪产业规模增长趋势数据
years = np.arange(2015, 2025)
industry_size = [2700, 3000, 3500, 2700, 4235, 6000, 5788, 8000, 8900, 9700]  # 单位：亿元
events = {
    2015: "冬奥申办成功",
    2018: "发展规划发布",
    2022: "冬奥举办",
    2023: "后奥运期",
    2024: "新周期",
}

# 设置柱状图的宽度和位置
bar_width = 0.4  # 柱状图的宽度（相对于年份间隔）
bar_x_offset = -bar_width / 2  # 柱状图相对于年份的中心点的x轴偏移量

plt.figure(figsize=(12, 6))

# 绘制折线图（金色加粗）
plt.plot(years, industry_size, color='#4CAF50', linewidth=2, label="产业规模折线图")

# 绘制柱状图
bar_years = [y + bar_x_offset for y in years]
bars = plt.bar(bar_years, industry_size, width=bar_width, color='#2196F3', alpha=0.8, label="产业规模柱状图")

# 设置x轴刻度与标签
plt.xticks(ticks=[y + bar_x_offset for y in years], labels=years.astype(str), rotation=45, ha='right')

# 在每个柱状图顶部添加数据量标签
for bar, size, year in zip(bars, industry_size, bar_years):
    yval = bar.get_height()
    plt.text(year, yval + 10, f"{size:.0f}亿", ha='center', va='bottom', fontsize=9, color='black')

# 标注关键事件
for year, event in events.items():
    idx = years.tolist().index(year)
    plt.axvline(x=year + bar_x_offset, color='r', linestyle='--', alpha=0.7)
    # 动态计算文本位置，避免重叠
    text_y = max(0, industry_size[idx] - (200 if year < 2023 else 300))  # 根据需要微调偏移量，避免超出图表范围
    plt.text(year + bar_x_offset, text_y, f"{event}\n({year})", ha='center', va='top', fontsize=9)

# 设置图表标题和轴标签
plt.title("冰雪运动规模增长趋势", fontsize=14, pad=20)
plt.xlabel("年份", fontsize=12)
plt.ylabel("产业规模 (亿元)", fontsize=12)

# 设置网格线和y轴范围
plt.grid(True, alpha=0.3)
plt.ylim(bottom=0, top=max(industry_size) * 1.1)

# 添加图例并调整位置
plt.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9), fontsize=10)

# 调整布局
plt.tight_layout()

# 显示图表
plt.show()