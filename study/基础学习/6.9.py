favorite_place={
    'liuqiangdong':{'1':'xian','2':'shanghai','3':'dazhou'},
    'zhaoli':{'1':'shanghai','2':'beijing','3':'chongqing'},
    'liwang':{'1':'chengdu','2':'fuzhou','3':'sjhsj'}
}
for name,text in favorite_place.items():
    print('name:'+name)
    for num,place in text.items():
        print("num:"+num)
        print("place:"+place)
