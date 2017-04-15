input_num = int(input())
num = input_num
count = 1

while True:
    res = num%10 + num//10
    num = int(str(num%10) + str(res%10))
    if input_num != num: count += 1
    else : break

print(count)

