l1 = []
l2 = []
d = {}

n = int(input("How many Student: "))

for i in range(n):
    l1.append(input("person: "))
    l2.append(int(input("person's marks: ")))

print(l1)
print(l2)

for j in range(n):
    if l2[j] >= 80:
        d[l1[j]] = (l2[j], "A+")
    elif l2[j] >= 70 and l2[j] <= 79:
        d[l1[j]] = (l2[j],"A")
    else:
        d[l1[j]] = (l2[j],"F")
print(d)