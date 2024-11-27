def count_profit(arr):
    max_profit = 0
    mini= 10000
    for i in arr:
        if i < mini:
            mini = i
        else:
            profit = i-mini
            max_profit = max(max_profit,profit)
    return max_profit





arr = [44,30,24,32,35,30,40,38,15]
print(count_profit(arr))