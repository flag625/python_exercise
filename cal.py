def cal(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
nums=[1,2,3,4,5]
print(cal(*nums))