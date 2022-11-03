d ={}
l1 = []
l2 = []


n = int(input("how many student:  "))
for i in range(n):
    name = str(input("The Name: "))
    number = int(input("Makes: "))
    gread = str(input("grade: "))
    d[name] = (number,gread)
print(d)

for keys in d:
    l2.append(d[keys][0])
for key, value in d.items():
    l1.append(key)

print(l1)
print(l2)