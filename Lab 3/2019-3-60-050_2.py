input1 = int(input("Enter Your Number: "))

n1 = 0
n2 = 1
cnt = 2
res = [0, 1]

if input1 == 0:
    print(0)
else:
    while True:
        # print('flg')
        tmp = n1 + n2
        n1 = n2
        n2 = tmp
        if n2 > input1:
            break
        res.append(n2)

        # cnt += 1

    print(res)
