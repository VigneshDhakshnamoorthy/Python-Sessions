a = "School master"
b = "The classroom"
print(a)
print(b)

a = sorted(str(a).replace(" ", "").lower())
b = sorted(str(b).replace(" ", "").lower())
print(a)
print(b)

a = ''.join(a)
b = ''.join(b)
print(a)
print(b)

if a == b:
    print("Both Words Are Anagram")
else:
    print("Both Words Are Not Anagram")

