def make_shirt(num,word):
    print("thie tshirt is"+num+"\nits on:"+word)
make_shirt(num='2',word='happy')
def get_formatted_name(first_name,last_name):
    full_name=last_name+" "+first_name
    return full_name.title()
musician=get_formatted_name('jinxin','liu')
print(musician)
def city_country(city,country):
    citycountry=city+","+country
    return citycountry
text=city_country('chengdu','china')
print(text)