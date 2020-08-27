s="acbdbcaddcba"
l = []
for i in s:
    if i not in l:
        l.append(i)

for i in range(len(l)):
    if i < (len(l)-1):
        if ord(l[i]) > ord(l[i+1]):
            l[i],l[i+1] = l[i+1],l[i]
result = "".join(l)
print(result)


# result = "".join(sorted(l))
# print(result)