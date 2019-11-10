liu={'first_name':'jinxin','last_name':'liu','age':'20','city':'chengdu'}
print(liu)
favorite_num={'a':'2','b':'4','c':'6'}
for k,v in favorite_num.items():
    print('key:'+k)
    print('v:'+v)
for name in favorite_num.keys():
    print(name)
for num in favorite_num.values():
    print(num)
li={'first_name':'fang','last_name':'li','age':'23','city':'xian'}
zhao={'first_name':'qiang','last_name':'zhao','age':'21','city':'guangzhou'}
people=[liu,li,zhao]
for person in people:
    print(person)