def make_album(singer_name,cd_name,num=''):#kongbaizifuchuan
    text={'singer':singer_name,'cd':cd_name}
    if num:
        text["num"]=num
    return text
one=make_album('zhoujielun','daoxiang',num=27)
two=make_album('linjunjie','jiangnan')
three=make_album('naying','mo')
print(one)
print(two)
print(three)
