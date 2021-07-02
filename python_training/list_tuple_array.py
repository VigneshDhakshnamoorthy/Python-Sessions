l = [1,2,3,4,5,5,6,7,33]
s = (1,2,3,4,5)
d = {1,2,3,4,5}
print(l)
l.append(6)
l.pop(4)
l.remove(33)
print(l)
ct = set(l)
print(ct)
for c in ct:
    print(c,"=",l.count(c))
ct.add(8)
ct.remove(2)
print(ct)