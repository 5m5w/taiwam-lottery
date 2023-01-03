# 同一網頁，點選不同的資料，網址卻沒變，可懷疑為post()方法
# 可以透過開發人員模式 -> Network做驗證request的方法為何
# 例如大樂透的網頁上，選擇了年/月後，網址都沒變，因此到network後，發現是post()

import requests
import pandas as pd
import sqlite3

conn = sqlite3.connect('中獎號碼.db')

d1 = pd.date_range('20210101', '20210630', freq='m')

for i in d1:
    # 看youtube解釋
    y = str(int(str(i)[:4])-1911)
    m = str(int(str(i)[5:7]))
    print(f'{y}年 {m}月')
    print("-----")

    url = "https://www.taiwanlottery.com.tw/lotto/lotto649/history.aspx"
    
    # 在 network -> payload找到form data，最下方有像是字典的資料型態，選擇111年5月。將資料放入payload
    payload={'__VIEWSTATE':'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',
    '__VIEWSTATEGENERATOR':'11E838D2',
    '__EVENTVALIDATION': 'WhiFxugkRCZkad2v26Uo3LJEHlAmQ5E5L0ZaNNsarjB3OqZ1jAbi0RWhRZR5nCCFe0dQK/I1zVC7KKvIhx2kX4mQ5VZr1GC7LuJIBfxqNWD2Drxw6ZKmxveSvTZzypcO2s+xAMwQNIZBEcU0psiTtNYjrw0bxEEE4iiywJOwePSY2Di+ld2A3iEHo3A7tXEW4lQiKnAsYRalBgln3Saq0rZKj28pDqzWj/Gu855ywjxZPTngT/HHP6VgyHmUD9NENIkhESVYkPovGSw54I+kNIOgalipROs82PaKHX2KlllDWPWtKYxi2MErp+fVraQt9b1ncD9k2KDTrMRy88HL2rv0fHhoBUAJ/tzZYSkDiY3cT7xeXtzwE5bLX2W12hN4fWBHi3u6FJGEDM6BUT0R9cryq8CXtAgDYOY+kHG6KjpWOQwXs9G0qX2oxa1n9gevw+aj5++/0jyC0QZF7bQDOhcnj2uDz41OWoPHYmGpoBUhflaI8RmAq96cUEUPkZJTZus13dIiPUpvCnYb3eaT4dYhNv3NGtLCzN+zBADMqpcPUok16XSHBP0CLSf3pw0QBhcOH2z2AsGW9IKQAxOVcW6OEk4BbAZjdhJYAVxk2ymjpDo0J9JncNtf2TTHWQPFc8vmYCuokCngGLqDMfvrUatTO7I=',
    'forma':'請選擇遊戲',
    'Lotto649Control_history$txtNO': '',
    'Lotto649Control_history$chk': 'radYM',
    'Lotto649Control_history$dropYear': y,
    'Lotto649Control_history$dropMonth':m,
    'Lotto649Control_history$btnSubmit':'查詢'}
    
    # requests post 讀取，並加入payload資料(111/11)，
    resp = requests.post(url, data=payload)
    
    # 寫入新建的'大樂透.html'
    # 輸出成html檔也不一定需要了，可以直接刪除
    with open('大樂透'+y+m+'.html', 'w', encoding='utf-8') as fobj:
        fobj.write(resp.text)
        
    #透過read_html將讀出來的陣列存入list1
    list1 = pd.read_html(resp.text)
    
    colName = ['期別', '開獎日', '兌獎截止', '銷售金額', '獎金總額', '獎號1', '獎號2', '獎號3', '獎號4', '獎號5', '獎號6', '特別號']
    
    for d in list1[2:10]:
        data=[]
        data.append(d.iloc[1,0]) #期別
        data.append(d.iloc[1,1]) #開獎日
        data.append(d.iloc[1,3]) #兌獎截止
        data.append(d.iloc[1,5]) #銷售金額
        data.append(d.iloc[1,7]) #獎金總額
        for i in range(2,9): #六個中獎號與一個特別號
            data.append(d.iloc[4,i])
        dftemp=pd.DataFrame([data], columns=colName)
        print(dftemp)
        # 在寫入進去sqlite前，要先檢查，是否已經有新增過該期別的資料，如果有，就不應該新增進去，用Select from來讀資料庫
        sql = 'Select * from 大樂透 where 期別="' + data[0] + '"'
        # 用try except來確認，是否已經有大樂透資料表，如果發生error，就會執行except建立一個空的Dataframe
        try:
            dfcheck = pd.read_sql(sql, conn)
        except:
            dfcheck = pd.DataFrame(columns=colName)
            
        if len(dfcheck) == 0:
            dftemp.to_sql('大樂透', conn, if_exists='append', index=False)
        print("--------")