'''
    test task
'''

import pandas as pd
import sys

sys.stdout.reconfigure(encoding='utf-8')

df = pd.read_excel("data.xlsx")

actual_month = 6

df = df.rename(columns={'new/current': 'deal'})
sale_column = df.loc[:, 'sale']
sellers_dict_sells = set(sale_column)
sellers_dict_sells.discard('-')
sellers_dict_sells = {x:0 for x in sellers_dict_sells if x==x}

for i in df.index:
    status, document, seller, month_deal, deal_sum, deal  = df[['status', 'document', 'sale', 'receiving_date', 'sum', 'deal']].iloc[i]
    try:
        month_deal = month_deal.month
        if int(month_deal) > actual_month:
            if deal == 'новая':
                if status == 'ОПЛАЧЕНО' and document =='оригинал':
                    new_deal = 0.07*deal_sum
                    sellers_dict_sells[seller] += new_deal
            elif deal == 'текущая':
                if status != 'ПРОСРОЧЕНО' and document =='оригинал':
                    if deal_sum > 10000:
                        actual_deal = 0.05*deal_sum
                    else:
                        actual_deal = 0.03*deal_sum
                    sellers_dict_sells[seller] += actual_deal
    except:
        ...

result = pd.DataFrame.from_dict(sellers_dict_sells, orient='index', columns = ['sum'])

print(result)