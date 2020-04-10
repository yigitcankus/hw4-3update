import pandas as pd
import numpy as np
import scipy
import warnings
import matplotlib as plt
warnings.filterwarnings('ignore')

"""
Veri kümesinde yer alan değişkenlerinin tiplerini ve her bir değişkenin eksik (null) değer oranını bulun.
"""
"""
primary key, state ve, year kategorik değişkenler, diğerleri sürekli değişken.
"""
states = pd.read_csv("states_all.csv")
# print(states.info())
#print(states.isnull().sum())
#print(states.isnull().count())
# print(states.isnull().sum()/states.isnull().count()*100)

######2
"""
Verimizde yıl (year) sütunu olduğunu farketmişsinizdir.
Şimdilik yıl verisini unutun ve her bir gözlemin aynı yıl içerisinde yapıldığını farz edin. 
Her bir değişken için eksik değerleri nasıl doldurabileceğinizi düşünün. 
Eksik değerleri bir değerle doldurmak hangi değişkenler için anlamlı, hangileri için anlamsızdır?
"""
# #for sutun_adi in states:
# #     for deger in states[sutun_adi]:
# #         if pd.isna(deger):
# #             states[sutun_adi].fillna(states[sutun_adi].mean(), inplace=True)

"""
Sayısal olan sürekli değişkenler için mantıklı olabilir. Ama State ve primarykey için doğru olacğaını sanmıyorum.
"""

######3
"""
Şimdi zaman faktörünü dikkate alma zamanı! 
2. sorudaki cevabınızı tekrar gözden geçirin ve eksik verileri o yıl içerisinde gözlemlenen değerlere dayanarak doldurun. 
Örneğin, bir değeri ortalama değer ile doldurmak isterseniz, o yılın ortalamasını hesaplayın.
"""

fill_list = ["ENROLL", "TOTAL_REVENUE", "FEDERAL_REVENUE",
             "STATE_REVENUE", "LOCAL_REVENUE", "TOTAL_EXPENDITURE",
             "INSTRUCTION_EXPENDITURE", "SUPPORT_SERVICES_EXPENDITURE",
             "OTHER_EXPENDITURE", "CAPITAL_OUTLAY_EXPENDITURE", "GRADES_PK_G",
             "GRADES_KG_G", "GRADES_4_G", "GRADES_8_G", "GRADES_12_G", "GRADES_1_8_G",
             "GRADES_9_12_G", "GRADES_ALL_G"]
print(states.isnull().sum()/states.isnull().count())

years = states["YEAR"].unique()
for col in fill_list:
    for year in years:
        states.loc[states["YEAR"] == year, col].fillna(states[states["YEAR"] == year][col].mean(), inplace=True)

# sns.heatmap(states.isnull(),yticklabels=False,cbar=False,cmap='viridis')
# plt.show()

print(states.isnull().sum()/states.isnull().count())

# yillar = states["YEAR"].unique()
#
# for yil in yillar:
#     print(states[states["YEAR"] == yil])
#
#
# sutun_list = states.columns
# print(sutun_list)
#
# for sutun in sutun_list:
#     if states[sutun].dtype == float:
#         states.fillna(states.mean(), inplace=True)
#
#
#
#
# print(states.isnull().sum()/states.isnull().count()*100)
# print(states.head(20))


#######4
"""
Bu sefer, eksik değerleri enterpolasyon yaparak doldurun.
"""

# states = states.interpolate()
# print(states.head(20))