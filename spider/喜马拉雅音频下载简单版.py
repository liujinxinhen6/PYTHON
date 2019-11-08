import requests
import parsel
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}


def download(medium_url, medium_name):
    path ='G:\喜马拉雅\阴间神探'
    response =requests.get(medium_url, headers=headers)
    with open(path + '\{}.mp4'.format(medium_name), 'wb') as f:
        f.write(response.content)


# medium_url = 'https://fdfs.xmcdn.com/group62/M08/E2/C4/wKgMZ10XalSTUIA4AIY_fqxrkIw813.m4a'
# download(medium_url, 'gg')
#


def get_api(trackId):
        api_url = f'https://www.ximalaya.com/revision/play/v1/audio?id={trackId}&ptype=1'
        response = requests.get(api_url, headers=headers)
        data = response.json()
        src = data['data']['src']
        return src


def get_HTMLpage(pageurl):
    response = requests.get(pageurl, headers=headers)
    response.encoding = response.apparent_encoding
    sel = parsel.Selector(response.text)
    soundlist = sel.css('.sound-list ul li a')
    for sound in soundlist[:30]:
        href = sound.css('a::attr(''href)').extract_first()
        medium_id = href.split('/')[-1]
        title = sound.css('a::attr(title)').extract_first()
        yield medium_id, title

    # print(href)
    # print(title)
    # print(type(href))
    # print(type(title))
    # #print(soundlist)


if __name__ == '__main__':

    for page in range(1,24):
        medium = get_HTMLpage('https://www.ximalaya.com/youshengshu/12642314/p'+str(page))
        for id,name in medium:
            download(get_api(id), name)



