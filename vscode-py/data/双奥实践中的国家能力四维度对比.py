import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family='YouYuan')
# ========================
# 数据准备与维度定义
# ========================
# 国家能力四个维度
categories = ['强制能力', '汲取能力', '渗透能力', '协商能力']

# 数据映射说明：
# 强制能力 = 奥运奖牌榜数量
# 汲取能力 = 奥运会对GDP的贡献
# 渗透能力 = 奥运会后全民健身参与率
# 协商能力 = 就业岗位数

# 模拟数据（评分范围1-10分）
scores_2008 = [8.5, 6.2, 5.8, 6.5]  # 2008年夏奥会
scores_2022 = [9.2, 8.5, 8.7, 9.0]  # 2022年冬奥会

# ========================
# 雷达图高级定制化配置
# ========================
# 设置极坐标参数
angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
angles += angles[:1]  # 闭合图形

# 创建画布
plt.figure(figsize=(10, 10))
ax = plt.subplot(111, polar=True)

# 颜色配置（精确匹配HEX值）
colors = {
    "2008": "#4CAF50",  # Material Design绿色
    "2022": "#2196F3"   # Material Design蓝色
}

# 绘制2008年数据（带边缘描边）
ax.plot(angles, scores_2008 + scores_2008[:1], 
        color=colors["2008"], 
        linewidth=2.5, 
        linestyle='-',
        marker='o',
        markersize=8,
        markerfacecolor='white',
        markeredgewidth=1.5,
        label='2008夏奥会')
ax.fill(angles, scores_2008 + scores_2008[:1], color=colors["2008"], alpha=0.15)

# 绘制2022年数据（带科技感渐变）
ax.plot(angles, scores_2022 + scores_2022[:1], 
        color=colors["2022"], 
        linewidth=2.5, 
        linestyle='-',
        marker='D',
        markersize=8,
        markerfacecolor='white',
        markeredgewidth=1.5,
        label='2022冬奥会')
ax.fill(angles, scores_2022 + scores_2022[:1], color=colors["2022"], alpha=0.15)

# ========================
# 高级可视化优化
# ========================
# 1. 极坐标网格定制
ax.set_theta_offset(np.pi/2)                # 起始角度在正上方
ax.set_theta_direction(-1)                  # 顺时针方向
ax.set_rgrids([2,4,6,8,10], angle=315)      # 径向网格线角度

# 2. 网格线样式强化
ax.yaxis.grid(True, 
             linestyle=(0, (5, 5)),        # 虚线模式：5pt实线+5pt空白
             linewidth=1.2,
             alpha=0.6,
             color='#607D8B')              # 蓝灰色网格线

# 3. 坐标轴标签增强
ax.tick_params(axis='both', 
              which='major',
              labelsize=12,
              labelcolor='#424242',        # 深灰色标签
              pad=15)                      # 标签间距

# 4. 维度标签美学设计
plt.xticks(angles[:-1], 
           categories,
           fontsize=13,
           fontfamily='Microsoft YaHei',   # 中文字体适配
           color='#212121',
           fontweight='semibold')

# 5. 数值标签动态标注
for angle, score_08, score_22 in zip(angles[:-1], scores_2008, scores_2022):
    y = max(score_08, score_22) + 0.5  # 动态计算y坐标
    ax.text(angle, y, 
            f"{score_08:.1f}|{score_22:.1f}",  # 显示双数据点
            ha='center', 
            va='center',
            fontsize=10,
            color='#616161')

# 6. 图例与标题专业排版
plt.title("双奥实践中国家能力四维度演进分析\n——基于赛事经济与社会效能的量化评估",
         fontsize=16,
         fontweight='bold',
         pad=35,
         color='#263238')
plt.legend(loc='upper right',
          bbox_to_anchor=(1.28, 1.12),
          frameon=True,
          framealpha=0.9,
          edgecolor='#CFD8DC')

# ========================
# 输出与保存
# ========================
plt.tight_layout()
plt.show()