# 1. 正则表达式
import re
# \w 匹配字母数字及下划线 \W 取反
print(re.findall('\w','hello egon 123'))
print(re.findall('\W','hello egon 123'))

# \s 匹配任意空白字符，等价于[\r\n\t\f] \S 取反
print(re.findall('\s','hello  egon  123'))
print(re.findall('\S','hello  egon  123'))

# \d 匹配任意数字，等价于[0-9] \D 取反
print(re.findall('\d','hello egon 123'))
print(re.findall('\D','hello egon 123'))

# \A 只匹配起始位置，不匹配结束查找
print(re.findall('\Aegon','hello egon 123'))
print(re.findall('^egon','hello egon 123'))

# $ == \Z 只匹配行结束位置，换行结束
print(re.findall('egon\Z','hello egon 123'))
print(re.findall('egon$','hello egon 123'))

# \n 匹配一个换行符
print(re.findall('\n','hello egon 123'))

# \t 匹配一个制表符
print(re.findall('\t','hello egon 123'))

# . 匹配除换行符外的任意一个字符；使用re.DOTALL参数，匹配所有任意一个字符；
print(re.findall('e.on','hello egon 123'))
print(re.findall('e.on','hello egon 123', re.DOTALL))

# ? 匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
print(re.findall('egon?','hello egon 123'))

# * 匹配前面那个字符出现0个或无穷个  ===> 非贪婪模式
print(re.findall('egon*','hello egonnn 123'))

# + 匹配前面那个字符出现1个或无穷个
print(re.findall('eon+','hello egonnn 123'))

# {m, n} 匹配前面一个字符，出现m次到n次
# 实现?号匹配
print(re.findall('e{0, 1}on','hello egonnn 123'))
# 实现*号匹配
print(re.findall('e{0,}on','hello egonnn 123'))
# 实现+号匹配
print(re.findall('egon{1, }','hello eegonnn 123'))

# .* 匹配任意长度，且任意的字符  ===> 贪婪模式
print(re.findall('e.*on','hello egonnn 123'))

# .*? 匹配任意长度，且任意的字符；*后面? 代表非贪婪匹配
print(re.findall('e.*?on', 'hello egonnn 123'))

# () 分组作用，表达式正常匹配，但只返回括号内的字符串
print(re.findall('(alex)_sb', 'alex_sb asdfdhjahfalex_sb'))

# [] 用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'；中括号里使用 ^ 代表取反；
print(re.findall('[egon]','hello egon 123'))
print(re.findall('[^egon]','hello egon 123'))

# | 或者 (?:) 小括号内 ?: 代表匹配成功的所有内容，而不仅仅是括号内的内容
print(re.findall('egon(?:s|es)','hello egons 123 egones'))

# 2. re的其他方法
import re
print(re.findall('egon(?:s|es)','hello egons 123 egones'))

# 查找所以包含的字符串，返回一个对象；使用 group方法获取一个值
print(re.search('egon(?:s|es)','hello egons 123 egones').group())

# match 就是 ^必须开头就匹配的search，返回一个对象；使用 group方法获取一个值
print(re.match('egon(?:s|es)','egons 123 egones').group())

# split 多个分隔符拆分字符串
print(re.split('[ :\\\/]', r'got :a.txt\3333/rwx'))

# sub 替换，字符串位置互换
print(re.sub('^egon', 'Egon', 'egon is beautful egon'))
print(re.sub('(.*?)(egon)(.*?)(egon)(.*)', r'\1\2\3Egon\5', '123 egon is beautful egon 123'))
print(re.sub('(lqz)(.*?)(SB)', r'\3\2\1', 'lqz is SB'))
print(re.sub('([a-zA-Z]+)([^a-zA-Z]+)([a-zA-Z]+)([^a-zA-Z]+)([a-zA-Z]+)', r'\5\2\3\4\1', 'lqz is SB'))

# compile
patten = re.compile('egon')
print(re.findall(patten, 'hello egons 123 egones'))


