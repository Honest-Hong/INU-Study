
a=input()
if int(a)<10:
    a = "0" + a
result = a
cnt=0

while 1:
    temp = int(a[0]) + int(a[1])
    temp2 = a[1] + str(temp%10)
    a = str(temp2)
    cnt = cnt + 1
    if result == a:
        break

print(cnt)
