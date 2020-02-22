input1 = int(input())
input2 = input()
dmojistan = input()
pegland = input()

dmojistan = dmojistan.split(" ")
dmojistan = list(map(int, dmojistan)) #turns string list into int list
pegland = pegland.split (" ")
pegland = list(map(int, pegland))
maxList = []
minList = []

def max(a, b):
    if a>=b:
        return a
    else:
        return b
if input1 == 1:
    dmojistan.sort()
    pegland.sort()
    for i in range (0, len(pegland), 1):
        minList.append(max(int(dmojistan[i]), int(pegland[i])))
    minSpeed = sum(minList)
    print (minSpeed)
elif input1 == 2:
    dmojistan.sort()
    pegland.sort(reverse=True)
    for i in range(0, len(pegland), 1):
        maxList.append(max(int((dmojistan[i])), int(pegland[i])))
    maxSpeed = sum(maxList)
    print(maxSpeed)
exit()


