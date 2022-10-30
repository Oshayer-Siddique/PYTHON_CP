print("Binary to decimal")
bin_num = list(input())
value = 0
for i in range(len(bin_num)):
    digit = bin_num.pop()
    if digit == '1':
        value = value + pow(2, i)

print(value)
print(type(value))