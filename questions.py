"""
    test questions
"""

import pandas as pd
import matplotlib.pyplot as plt
import sys

sys.stdout.reconfigure(encoding='utf-8')

df = pd.read_excel("data.xlsx")
#1-е задание
status_column = df.loc[:, 'status']

june_2021_index = status_column.tolist().index('Июнь 2021')
jule_2021_index = status_column.tolist().index('Июль 2021')

df_june_temp = df.iloc[june_2021_index+1:jule_2021_index] #+1 для исключения названия месяца
df_june_lost = df_june_temp.loc[df['status'] != 'ПРОСРОЧЕНО']

sum_column = df_june_lost.loc[:, 'sum']
june_monthly_sum = sum([x for x in list(sum_column)])
print(june_monthly_sum)

#2-е задание
x=list(df_june_lost.index)
y=list(df_june_lost.loc[:, 'sum'])
plt.plot(x, y)
plt.xlabel('Сделки июнь 2021')
plt.ylabel('Выручка')
plt.title('Измениение выручки')
plt.show()

#3-е задание / изначально считал с просроченными платежами
sep_2021_index = status_column.tolist().index('Сентябрь 2021')
oct_2021_index = status_column.tolist().index('Октябрь 2021')

df_sep_temp = df.iloc[sep_2021_index+1:oct_2021_index]

sale_column = df_sep_temp.loc[:, 'sale']
sellers = list(set(list(sale_column)))
sellers_dict_sells = {}
for seller in sellers:
    df_name_seller_temp = df_sep_temp.query(f'sale.isin(["{seller}"])')
    sum_column = df_name_seller_temp.loc[:, 'sum']
    sep_seller_monthly_sum = sum([x for x in list(sum_column)])
    sellers_dict_sells[seller] = sep_seller_monthly_sum
print(max(sellers_dict_sells, key=sellers_dict_sells.get))

#4-е задание

df_oct_temp = df.iloc[oct_2021_index+1:]

df_new_name_deal = df_oct_temp.rename(columns={'new/current': 'deal'})
type_deal = df_new_name_deal.deal.value_counts().index.tolist()[0]    #По умолчанию возвращает данные по убыванию

print(type_deal)

# 5-е задание

rec_date_series = df_june_temp.loc[:, 'receiving_date'].loc[df['document'] == 'оригинал']
date_list = [x.month for x in list(rec_date_series)].count(5)       #май(5)
print(date_list)