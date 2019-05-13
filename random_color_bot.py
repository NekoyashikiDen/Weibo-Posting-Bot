#encoding=utf-8

import os
import time
import random
from weibo import APIClient

if __name__ == '__main__':
    app_key = '2386454502'
    app_secret = '79aba08d17affc525f95ac9e6d355d2a'
    callback_url = 'https://api.weibo.com/oauth2/default.html'
    passport_url = 'https://github.com/NekoyashikiDen'
    
    client = APIClient(app_key = app_key, app_secret = app_secret, redirect_uri = callback_url)
    auth_url = client.get_authorize_url()
    print('\n请访问以下地址，选择授权并返回Code值：\n', auth_url)
    code = input("\n输入Code：")
    try:
        r = client.request_access_token(code)
    except:
        print('获取令牌失败！请检查输入Code是否正确并重试。')
    else:
        client.set_access_token(r.access_token, r.expires_in)
        print('访问令牌：', r.access_token)
        print('剩余访问时间：', r.expires_in, '秒\n')
        
        '''count = 0
        while True:
            temp = random.randint(1, 22)
            pic = 'C:/Users/hasee/Desktop/random/' + str(temp) + '.jpg'
            fullpic = open(pic, 'rb')
            stR = 'Nagisa & Karuma Pic No.' + str(temp)
            fullstr = stR + passport_url
            
            try:
                client.statuses.share.post(status = fullstr, pic = fullpic)
            except:
                print('发送微博失败！请检查内容是否符合规范或令牌是否到期并重试。')
                break
            else:
                count = count + 1
                print('发送微博成功！累计第' + str(count) + '条。')
            
            fullpic.close()
            time.sleep(600)'''
        
        count = 0
        sTime = 15
        path = 'C:/Users/hasee/Desktop/randomcolor/'
        files = os.listdir(path)
        random.seed(time.time())
        random.shuffle(files)
        len = len(files)
        pic = 0
        print('所设置发送间隔：', sTime, '秒')
        
        while pic < len:
            stR = files[pic][:8]
            fullstr = stR + passport_url
            fullpic = open(path + files[pic], 'rb')
            
            try:
                client.statuses.share.post(status = fullstr, pic = fullpic)
            except:
                print('\n发送微博失败！请检查内容是否符合规范或令牌是否到期并重试。')
                break
            else:
                count += 1
                print('发送微博成功！累计第' + str(count) + '条。                ')
                fullpic.close()
                pic += 1
                
                for i in range(sTime):
                    print('下一条进度：', round((i + 0.01) * 100 / sTime), '%，预计剩余时间', round(sTime - i), '秒  ', end = '\r')
                    time.sleep(1)