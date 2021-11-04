import os

file_path_1 = os.path.join(os.getcwd(), '1.txt')
file_path_2 = os.path.join(os.getcwd(), '2.txt')
file_path_3 = os.path.join(os.getcwd(), '3.txt')
file_path_4 = os.path.join(os.getcwd(), 'res.txt')
file_dict = {} # словарь с именами, кол-вом строк
story_dict = {} # словать с текстом

# собираем данные с файлов в переменные
with open(file_path_1, 'r', encoding = 'utf-8') as file_1:
    story_1 = []
    counts_1 = 0
    file_name_1 = file_path_1[-5:]
    for strings in file_1:
        counts_1 += 1
        story_1.append(strings)
    file_dict[file_name_1] = counts_1 
    story_dict[file_name_1] = story_1
    # print(story_1)

with open(file_path_2, 'r', encoding = 'utf-8') as file_2:
    story_2 = []
    counts_2 = 0
    file_name_2 = file_path_2[-5:]
    for strings in file_2:
        counts_2 += 1
        story_2.append(strings)
    file_dict[file_name_2] = counts_2
    story_dict[file_name_2] = story_2
    # print(story_2)

with open(file_path_3, 'r', encoding = 'utf-8') as file_3:
    story_3 = []
    counts_3 = 0
    file_name_3 = file_path_3[-5:]
    for strings in file_3:
        counts_3 += 1
        story_3.append(strings)
    file_dict[file_name_3] = counts_3
    story_dict[file_name_3] = story_3
    # print(file_dict)



# сортировка файлов в словарях по кол-ву строк
sorted_values = sorted(file_dict.values()) 
file_dict_sorted = {}

for value in sorted_values:
    for key in file_dict.keys():
        if file_dict[key] == value:
            file_dict_sorted[key] = file_dict[key]
            break


sorted_keys = file_dict_sorted.keys()
story_dict_sorted = {}

for key in sorted_keys:
    for value in story_dict.values():
        if story_dict[key] == value:
            story_dict_sorted[key] = story_dict[key]
            break

print(story_dict_sorted)
print(file_dict_sorted)

# записываем данные в новый файл
with open(file_path_4, 'wt', encoding = 'utf-8') as file_4: 
    for name, string in file_dict_sorted.items():
        file_4.write(f'{name} \n {string} \n') 
        for story_name, story in story_dict_sorted.items():
            if story_name == name:
                for line in story:
                    file_4.write(line)
            else:
                continue


    
 
