import re
# 正则表达式必须引入re模块

# # a = 'hpython'
# # b = re.match('h', a).group()
# # # 匹配开头match,如果不符合要求立即停止
# # ,group是查询打印出匹配的字符
# # print(b)
# #$ 代表结尾 abc$
#  #  ^abc ^代表非abc中任意一个字符
# # . 代表匹配任意字符(除了\n)  \d 数字 \D非数字 \s 空白 \S 非空白
# # \w 字符 \W非单词字符
# # 量词字符  *
#
# # * 匹配前一个字符0次或者无限次
# # + 匹配前一个字符1次或者无限次
# # ? 匹配前一个字符0次或者1次
# # {m}/{m,n}扩展前一个字符0次或者无限次
# # *?/+?/?? 匹配模式变为非贪婪(即尽可能骚匹配字符)
# # (.*?)万能查找
#
#
# a = 'sssw1212fsafa23123sd21312'
# # b = re.search('\d+',a).group()
# # # search 直到找到第一个就立即停止,不查询后面的其他字符串
# # # findall会查询所有,不管前面是否查到,findall不需要group()字符串存到列表
# # print(b)
# # compile 添加正则表达师
# # res = re.compile('\d+')
# # b = re.findall(res, a)
# # print(b)
# # sub 替换
# # res = re.compile("\d+")
# # b = re.sub(res, '+', a)
# # print(b)
# # spite 分割
