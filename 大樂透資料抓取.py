#大樂透網路爬蟲

import pandas as pd
# pandas 是python界的excel

url = "https://www.taiwanlottery.com.tw/lotto/lotto649/history.aspx"
# 讀取網址

df=pd.read_html(url)
# 因讀取的資料是表格 所以是用 read_html

# for d in df[2:]:
#     # 看全部抓取的資料
#     # 資料從第2列開始
#     print(d.iloc[1,0])
#     print("-------")

# 點df看整個表格資料，抓取大樂透的特定數值
for d in df[2:12]:
    data=[]
    data.append(d.iloc[1,0]) #期別
    data.append(d.iloc[1,1]) #開獎日
    data.append(d.iloc[1,3]) #兌獎截止
    data.append(d.iloc[1,5]) #銷售金額
    data.append(d.iloc[1,7]) #獎金總額
    for i in range(2,9): #六個中獎號與一個特別號
        data.append(d.iloc[4,i])
# 中獎號在表格中的第四列，所以列固定在4，而從小到大的號碼，分別在第二欄至第八欄的位置，所以用for迴圈抓取
    print(data)    
    print("-----")
    
##第二部分##
colName = ['期別', '開獎日', '兌獎截止', '銷售金額', '獎金總額', '獎號1', '獎號2', '獎號3', '獎號4', '獎號5', '獎號6', '特別號' ]
lotto = pd.DataFrame(columns=colName)
# 只單純建立一個只有欄位名稱，沒有資料的DataFrame

