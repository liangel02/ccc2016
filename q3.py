def size(r):
    temp = []
    for p in range(len(r)):
        if p != len(r)-1 and r[p] == r[p+1]:
            a = r[p] * 2
            temp.append(a)
        elif (p + 2) <= (len(r) - 1) and r[p] == r[p+2]:
            b = r[p] + r[p+1] + r[p+2]
            temp.append(b)
        elif r[p] == r[p-2] or r[p] == r[p-1]:
            continue
        elif (p + 1) <= (len(r) - 1) and r[p+1] == r[p-1]:
            continue
        else:
            temp.append(r[p])
        print("printing temp")
        print(temp)
    if len(temp) == 0:
        return r
    r = temp
    return r


num = int(input())
rice = input()

rice = rice.split(" ")
rice = list(map(int, rice))


rice = size(rice)
print("function return")
print(rice)
for i in range(len(rice)):
    for m in range(i+1, len(rice)):
        if rice[i] == rice[m]:
            rice = size(rice)
            print("printing rice")
            print(rice)
            break
        else:
            continue
    if m == len(rice):
        continue

rice.sort()
print(rice[-1])
