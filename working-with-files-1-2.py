import os
import pprint

# ЗАДАЧА 1
file_path = os.path.join(os.getcwd(), 'recipes.txt')
with open(file_path, 'r', encoding = 'utf-8') as recipes:
    cook_book = {}
    for dish in recipes:
        dish_name = dish.strip()
        count = int(recipes.readline().strip())
        temp_list = []
        for ingredient in range(count):
            ingredient_name, quantity, measure = recipes.readline().split(' | ')
            temp_list.append(
                {'ingredient_name' : ingredient_name, 'quantity' : quantity, 'measure' : measure.strip() }
            )
        cook_book[dish_name] = temp_list
        recipes.readline()
    pprint.pprint(cook_book)

print('')


# ЗАДАЧА 2
def get_shop_list_by_dishes(dishes, person_count):
    temp_dict = {}
    temp_string = ''
    quant = 0
    for dish in dishes:
        for recipe, ingredients in cook_book.items():
            for element in ingredients:   
                if dish == recipe:
                    temp_string = element['ingredient_name']
                    # проверка на дублирование элементов и запись
                    quant = int(element['quantity'])
                    if temp_string in temp_dict.keys():
                        for ingred, inner_dict in temp_dict.items():
                            if ingred == temp_string:
                                quant = int(inner_dict['quantity'])
                            else:
                                continue  
                temp_dict[temp_string] = {'measure': element['measure'], 'quantity': quant * person_count}         
    pprint.pprint(temp_dict) 



get_shop_list_by_dishes(['Омлет','Фахитос'], 2)


