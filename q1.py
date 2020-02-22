input1 = input()
input2 = input()

word1 = list(input1)
word2 = list(input2)
flag = list()
flag1 = 0
for i in range (0, len(input1), 1):
    flag.append(0)
for n in range (0, len(input2), 1):
    flag1 = 0
    for i in range (0, len(input1), 1):
        if word2 [n] == "*":
            flag1 = 1
            break
        elif word1[i] == word2 [n] and flag [i] == 0:
            flag[i] = 1
            flag1 = 1
            break
        elif word1 [i] == word2 [n] and flag [i] == 1:
            continue
    if flag1 == 0:
        print ("N")
        exit ()
print ("A")

