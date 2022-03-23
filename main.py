cook_book = {}
with open('recipes.txt', encoding='utf-8') as file:
    while True:
        x = file.readline().strip()
        if not x:
            break
        else:
            cook_book[x] = []
            for b in range(int(file.readline().strip())):
                y = file.readline().strip().split("|")
                z = {}
                z['ingredient_name'] = y[0]
                z['quantity'] = y[1]
                z['measure'] = y[2]
                cook_book[x] += [z]
            file.readline()
print(cook_book)