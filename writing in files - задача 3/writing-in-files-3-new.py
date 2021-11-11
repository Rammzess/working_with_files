import os

file_dict = {} # словарь с именами, кол-вом строк
story_dict = {} # словарь с текстом
file_dict_sorted = {}
story_dict_sorted = {}

def file_read(file_name):
    file_path = os.path.join(os.getcwd(), file_name)
    with open(file_path, 'r', encoding = 'utf-8') as file:
        story = []
        counts = 0
        file_name = file_path[-5:]
        for strings in file:
            counts += 1
            story.append(strings)
        file_dict[file_name] = counts 
        story_dict[file_name] = story
    return file_dict, story_dict


def file_sort_files(file_dict):
    sorted_values = sorted(file_dict.values()) 

    for value in sorted_values:
        for key in file_dict.keys():
            if file_dict[key] == value:
                file_dict_sorted[key] = file_dict[key]
                break
    return file_dict_sorted
    
                
def file_sort_story(story_dict):
    sorted_keys = file_dict_sorted.keys() 

    for key in sorted_keys:
        for value in story_dict.values():
            if story_dict[key] == value:
                story_dict_sorted[key] = story_dict[key]
                break
    return story_dict_sorted

def file_write(file_name):
    file_path = os.path.join(os.getcwd(), file_name)
    with open(file_path, 'wt', encoding = 'utf-8') as file: 
        for name, string in file_dict_sorted.items():
            file.write(f'{name} \n {string} \n') 
            for story_name, story in story_dict_sorted.items():
                if story_name == name:
                    for line in story:
                        file.write(line)
                else:
                    continue
    return file_name              
                    
file_read('1.txt')
file_read('2.txt')
file_read('3.txt')
file_sort_files(file_dict)
file_sort_story(story_dict)
file_write('res.txt')
