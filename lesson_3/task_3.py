# Задание 3

def thesaurus(*args):
    dictionary_names = {}
    list_letters = []

    # Этот блок чтобы исключить повторение

    for name in args:
        list_letters.append(name[0])
    list_letters = list(set(list_letters))
    list_letters.sort()

    # Теперь не будет "дублирующих" итераций

    for let in list_letters:
        list_names = []
        for name in args:
            if name[0] == let:
                list_names.append(name)
        dictionary_names[let] = list_names
    return dictionary_names


names = ['Иван', 'Марина', 'Пётр', 'Саня', 'Илья', 'Паша', 'Марина']
print(thesaurus(*names))
