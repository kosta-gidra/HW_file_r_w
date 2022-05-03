import os

task_path = os.getcwd()
task_dir = 'sorted'
task_file_1 = '1.txt'
task_file_2 = '2.txt'
task_file_3 = '3.txt'
task_file_4 = '4.txt'
full_path_tf1 = os.path.join(task_path, task_dir, task_file_1)
full_path_tf2 = os.path.join(task_path, task_dir, task_file_2)
full_path_tf3 = os.path.join(task_path, task_dir, task_file_3)
full_path_tf4 = os.path.join(task_path, task_dir, task_file_4)


def get_task3():
    data_list = []
    with open(full_path_tf1, 'r', encoding='utf-8') as file:
        data1 = file.readlines()
        data_list.append(data1)
    with open(full_path_tf2, 'r', encoding='utf-8') as file:
        data2 = file.readlines()
        data_list.append(data2)
    with open(full_path_tf3, 'r', encoding='utf-8') as file:
        data3 = file.readlines()
        data_list.append(data3)
    data_list.sort(reverse=True)
    with open(full_path_tf4, 'w', encoding='utf-8') as file:
        file.write(''.join(data_list[0]))
        file.write(''.join(data_list[1]))
        file.write(''.join(data_list[2]))
    return


def get_dict(file_name='recipes.txt'):
    with open(file_name, 'r', encoding='utf-8') as file:
        cook_book = {}
        count = 0
        for line in file:
            if count == 0:
                cook_book[line.strip()] = []
                key = line.strip()
                ingredients = []
                count = -1
            elif count == -1:
                count = int(line) + 1
            elif ' | ' in line:
                ingredient = {}
                lst = line.strip().split(' | ')
                ingredient['ingredient_name'] = lst[0]
                ingredient['quantity'] = lst[1]
                ingredient['measure'] = lst[2]
                ingredients.append(ingredient)
                count -= 1
                if count == 1:
                    cook_book[key] = ingredients
            else:
                count -= 1
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    ingridients = {}
    for dish in dishes:
        for ingridient in get_dict()[dish]:
            if ingridient['ingredient_name'] not in ingridients:
                ing_measure = {'measure': (ingridient['measure']),
                               'quantity': int((ingridient['quantity'])) * person_count}
                ingridients[ingridient['ingredient_name']] = ing_measure
            else:
                dict_ = ingridients[ingridient['ingredient_name']]
                ing_measure = {'measure': (ingridient['measure']),
                               'quantity': int((ingridient['quantity'])) * person_count + dict_['quantity']}
                ingridients[ingridient['ingredient_name']] = ing_measure
    return ingridients


def show_dict(enter_dict):
    for key, value in enter_dict.items():
        print(f"'{key}': \n    {value}")
    return


show_dict(get_dict())
print()
show_dict(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 3))
get_task3()
