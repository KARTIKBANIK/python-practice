#Find the biggest number....

a = int(input('Number 1: '))
b = int(input('Number 2: '))
c = int(input('Number 3: '))

if a>b:
    if a>c:
        print(a, 'is the biggest.')
    else:
        print(c, 'is the biggest.')
else:
    if b>c:
        print(b, 'is the biggest.')
    else:
        print(c, 'is the biggest.')
    