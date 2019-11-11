import random
import requests




def sendRoll():
    url = 'https://api.live.bilibili.com/msg/send'
    cookie = '''_uuid=DD477B4C-372A-CF0F-8123-41D6A48002FE33756infoc; buvid3=B5B07660-965B-4F0F-AF9B-741F83481539190963infoc; LIVE_BUVID=AUTO8615687766341847; sid=j4zgo1ok; CURRENT_FNVAL=16; stardustvideo=1; rpdid=|(JY)J|R~)))0J'ulY)~~Y~~|; laboratory=1-1; UM_distinctid=16d9643703a38e-03c7ef5fbb8a2f-4c312373-144000-16d9643703b518; bp_t_offset_298099537=319093620300014904; CURRENT_QUALITY=80; DedeUserID=298099537; DedeUserID__ckMd5=5d850571f760986a; SESSDATA=5b863cce%2C1575127657%2C65a77da1; bili_jct=d01cfe5a1720f0379de611eea76bc3d8; _dfcaptcha=095cef5c9b442831cc476c53ba3f6a79; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1573134202,1573135074,1573137377; Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02=1573137377; finger=964b42c0; im_notify_type_298099537=0'''
    data = {
        'color':'16777215',
        'fontsize':'25',
        'mode': '1',
        'msg': words,
        'rnd': '1573128948',
        'roomid': '2434370',
        'bubble': '0',
        'csrf_token': 'bfad36583e71339c73b11d4877a9fcf0',
        'csrf': 'bfad36583e71339c73b11d4877a9fcf0'

    }
    headers= {

        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Content-Length': '160',
        'Origin': 'https://live.bilibili.com',
        'Connection': 'keep-alive',
        'Referer': 'https://live.bilibili.com/1361615',
        'Cookie':cookie

    }
    r = requests.post(url, data=data, headers=headers)


    print(r.text)







if __name__ == '__main__':
    words = input('请输入弹幕:')
    word = random.choice(words)
    print(word)
    sendRoll()


