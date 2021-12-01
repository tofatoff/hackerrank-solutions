# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
phonebook = {}

for _ in range(n):
    name,number = input().split()
    phonebook[name] = number
    
while True:
    try:
        name = input()
        if name in phonebook.keys():
            print(name+"="+phonebook[name])
        else:
            print("Not found")
    except:
        break
