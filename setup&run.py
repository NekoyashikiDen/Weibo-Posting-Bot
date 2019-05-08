#encoding=utf-8

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
    print('Access this site & copy the code number\n', auth_url)
    code = input("Input code: ")
    try:
        r = client.request_access_token(code)
    except:
        print('Accessing token failed! Please check the code and try again.')
    else:
        client.set_access_token(r.access_token, r.expires_in)
        print('Access token: ', r.access_token)
        print('Expire time: ', r.expires_in, 's')
        
        count = 0
        while True:
            fullstr = str(random.randint(x, x)) + passport_url
            fullpic = open('xxxxx.jpg', 'rb')
            
            try:
                client.statuses.share.post(status = fullstr, pic = fullpic)
            except:
                print('Posting failed! Please check the content or if the time expired and try again.')
            else:
                count = count + 1
                print('Posting succeeded! This is No.' + str(count) + '.')
            
            time.sleep(100)