t = int(input())

for i in range(t):
    s = input()
    for i in range(0,len(s),2):
        print(s[i],end="")
    print(end=" ")
    for i in range(1,len(s),2):
        print(s[i],end="")
    print()

