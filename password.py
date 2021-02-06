#密碼重試程式

#先把條件都設好 再下去思考
#先定義好後面不用再項一項修改
password = 'a123456' 
x = 3 #可試次數

while True:
    pwd = input('請輸入密碼: ')
    if pwd == password:
        print('登入成功!!')
        break #stop
    else:
        x = x - 1
        print('輸入錯誤 還有', x, '次機會')
        if x == 0:
            print('嘗試次數已達上限')
            break #stop
 
 