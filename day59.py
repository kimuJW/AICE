import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

fm.get_fontconfig_fonts()

font_list = [font.name for font in fm.fontManager.ttflist]
font_list

sns.set(font="NanumGothicCoding", 
        rc={"axes.unicode_minus":False}, 
        style='darkgrid')
ax = sns.countplot(x=df_total['level1_pnu'], palette = "RdBu")

x = df_total['signaltype'] # 샘플 생성

sns.distplot(x)
plt.show()

sns.boxplot(x = df_total['level1_pnu'], y = df_total['A_DISTANCE'], data = df_total, palette = "RdBu")
plt.show()

sns.boxplot(x = df_total['level1_pnu'], y = df_total['ET'], data = df_total, palette = "RdBu")
plt.show()

uniform_data = np.random.rand(10, 12) # 난수로 데이터 만들기
sns.heatmap(uniform_data)
plt.show()

sns.pairplot(df_total)
plt.show()

df_total.corr()
sns.heatmap(df_total.corr(), annot=True, cmap="RdBu")
plt.show()