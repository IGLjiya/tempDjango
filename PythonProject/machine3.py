a = ['car','cat','fear','center']
b = ['cat','dog','shatter','donut','at','todo','']

largest_word = ''
for i in b:
    if len(i)> len(largest_word):
        largest_word = i
print(largest_word)