pets={
'pet_0':{'master':'liuqiang','type':'dog'},
'pet_1':{'master':'lifang','type':'cat'},
'pet_2':{'master':'mating','type':'duck'}
}
for name,text in pets.items():
    print("name:" +name)
    master=text['master']
    type=text['type']
    print("\tmaster:"+master.title())
    print("\ttype:"+type.title())
