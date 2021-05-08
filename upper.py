name = input('Enter your name: ')
name = name.upper()
print(name)
mylist = [letter for letter in name]
mylist.reverse()
for letter in mylist:
    print(letter, end="")