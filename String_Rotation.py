l = []
s = ""
vowel = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
count = 1
string = input()
x = int(input())
for i in string:
    ascii = ord(i) + x
    if i.isupper():
        for j in range(26, 26 + x, 26):
            if ascii > 90 and ascii < 90 + j:
                ascii = ascii - count * (26)
                break
            else:
                count += 1
    elif i.islower():
        for k in range(26, 26 + x, 26):
            if ascii > 122 and ascii < 122 + k:
                ascii = ascii - count * (26)
                break
            else:
                count += 1
    l.append(ascii)
    count = 1
for m in l:
    s = s + chr(m)
print(s)
if s.startswith(vowel) and s.endswith(vowel):
    print("Happy Cool String")
else:
    print("Happy Hot String")
