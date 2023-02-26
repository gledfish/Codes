import re     

phone_number_Regex = re.compile(r'(\d\d\d)-(\d\d\d\d\d\d\d\d)') # 获得正则表达式
# () 可以对正则表达式进行分组

mo = phone_number_Regex.search("My number is 185-91052870.") # 在表达式中寻找match的字符
print(mo.group(1)) # 185
print(mo.groups()) # (185, 91052870)

heroRegex = re.compile(r'Batman|Tina Fey')
# 空格会计入字符
match = heroRegex.search('I am hero Batman.')
print(match.group())  # batman

batRegex = re.compile(r'Bat(man|men|woman|women)')
match = batRegex.search('Batwomen')
print(match.group()) # Batwomen

batRegex = re.compile(r'BAT(WO)?MAN') # ?进行选择
match = batRegex.search('BATMAN')
print(match.group()) # BATMAN
match = batRegex.search('BATWOMAN')
print(match.group()) # BATWOMAN

#还有其他的正则表达式如下
# ()* ：将括号内的内容匹配 0 次或者多次
#（）+ ：匹配 1 次或者多次
#（）{n} ：指定匹配n次

#贪心匹配
greedyRegex = re.compile(r'(Ha){3,5}')
match = greedyRegex.search('HaHaHaHaHa') # 默认贪心模式，匹配五次
print(match.group())  # HaHaHaHaHa
# 非贪心匹配
greedyRegex = re.compile(r'(Ha){3,5}?')
match = greedyRegex.search('HaHaHaHaHa')  # 非贪心模式，匹配三次
print(match.group())  # HaHaHa

# Regax.findall('') 返回所有匹配的文本
