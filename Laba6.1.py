st = input('Введите строку: ')
space_1 = 0
space_2 = 0

for x in range(len(st)):
    if st[x] == " ":
        if space_1 == 0:
            space_1 = x
        space_2 = x
if space_1 == space_2:
    print("")
else:
    print(st[space_1 + 1:space_2])
