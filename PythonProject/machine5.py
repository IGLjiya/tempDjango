import re


x = open("text.txt",'r')
list2 = list(re.split('\s',x.read()))
print(list2.count('the'))

