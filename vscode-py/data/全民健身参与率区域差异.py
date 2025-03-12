import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rc('font', family='YouYuan')

# 全民健身参与率热力图
import seaborn as sns

# 模拟数据
provinces = ['北京', '天津', '河北', '山西', '内蒙古', 
            '辽宁', '吉林', '黑龙江', '上海', '江苏',
            '浙江', '安徽', '福建', '江西', '山东',
            '河南', '湖北', '湖南', '广东', '广西',
            '海南', '重庆', '四川', '贵州', '云南',
            '西藏', '陕西', '甘肃', '青海', '宁夏', '新疆']

np.random.seed(42)
participation = np.random.randint(25, 50, size=len(provinces))

# 创建数据框
df = pd.DataFrame({'省份': provinces, '参与率': participation})
df = df.sort_values('参与率', ascending=False)

# 转换为矩阵格式
heatmap_data = df.set_index('省份').T

plt.figure(figsize=(12, 8))
sns.heatmap(heatmap_data, cmap='coolwarm', annot=True, fmt="d",
           cbar_kws={'label': '参与率 (%)'},
           annot_kws={'fontsize': 12, 'color': 'black'})

# 标记重点城市
highlight = ['北京', '上海', '兰州']
for label in plt.gca().get_xticklabels():
    if label.get_text() in highlight:
        label.set_color('gold')
        label.set_fontweight('bold')

plt.title("全民健身参与率区域差异", pad=20)
plt.xticks(rotation=45)
plt.tight_layout()

# 添加数据来源和备注
plt.figtext(0.5, -0.05, "数据来源: 模拟数据\n备注: 参与率为随机生成，仅供示例使用", 
            ha="center", fontsize=10, color='#424242')

plt.show()














