#encoding=utf-8

import os
import time
import random
from weibo import APIClient

if __name__ == '__main__':
    app_key = 'xxxxxxxxx'
    app_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    callback_url = 'https://api.weibo.com/oauth2/default.html'
    passport_url = 'xxxxxxxxxxxxxxxxxxxxx'
    
    client = APIClient(app_key = app_key, app_secret = app_secret, redirect_uri = callback_url)
    auth_url = client.get_authorize_url()
    print('\nAccess this site & copy the code number\n', auth_url)
    code = input("\nInput code: ")
    try:
        r = client.request_access_token(code)
    except:
        print('Accessing token failed! Please check the code and try again.')
    else:
        client.set_access_token(r.access_token, r.expires_in)
        print('Access token: ', r.access_token)
        print('Expire time: ', r.expires_in, 's\n')
        
        count = 0
        sTime = 60
        path = 'C:/randomcolor/'
        files = os.listdir(path)
        random.seed(time.time())
        random.shuffle(files)
        len = len(files)
        pic = 0
        print('Post time set: ', sTime, 's')
        
        while pic < len:
            stR = files[pic][:8]
            fullstr = stR + passport_url
            fullpic = open(path + files[pic], 'rb')
            
            try:
                client.statuses.share.post(status = fullstr, pic = fullpic)
            except:
                print('\nPosting failed! Please check the content or if the time expired and try again.')
                break
            else:
                count += 1
                print('Posting succeeded! This is No.' + str(count) + '.                ')
                fullpic.close()
                pic += 1
                
                for i in range(sTime):
                    print('Next post process: ', round((i + 0.01) * 100 / sTime), '%, expected in', round(sTime - i), 's  ', end = '\r')
                    time.sleep(1)
