import json

with open('recipes.txt', encoding='utf-8') as file:
    cook_book = {}
    while True:
        dish = file.readline().strip()
        if not dish:
            break
        else:
            cook_book[dish] = []
            for ingredient in range(int(file.readline().strip())):
                ingredient = file.readline().strip().split("|")
                ingredients = {'ingredient_name' : ingredient[0], 'quantity' : ingredient[1], 'measure' : ingredient[2]}
                cook_book[dish] += [ingredients]
            file.readline()
# print(f'cook_book = {json.dumps(cook_book, indent=4, ensure_ascii=False)}')


def get_shop_list_by_dishes(dishes, person_count):
    list_of_products = {}
    for person in range(person_count):
        for dish in dishes:
            for prod in cook_book[dish]:
                if prod['ingredient_name'] in list_of_products:
                    list_of_products[prod['ingredient_name']]['quantity'] += int(prod['quantity'])
                else:
                    list_of_products[prod['ingredient_name']] = {'measure' : prod['measure'], 'quantity' : int(prod['quantity'])}

    print(json.dumps(list_of_products, ensure_ascii=False, indent=2))


get_shop_list_by_dishes(['Омлет', 'Омлет'], 1)