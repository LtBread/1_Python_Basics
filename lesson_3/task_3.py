# Задание 3

def thesaurus(*args):
    dictionary_names = {}
    list_letters = []

    # Этот блок чтобы исключить повторение
    for name in args:
        list_letters.append(name[0])
    list_letters = set(list_letters)
    list_letters = list(list_letters)
    list_letters.sort()

    # Теперь не будет "дублирующих" итераций
    for let in list_letters:
        list_names = []
        for name in args:
            if name[0] == let:
                list_names.append(name)
        dictionary_names[let] = list_names
    return dictionary_names


def thesaurus_adv(*args):
    list_letters = []

    for let in args:
        let = let.split()
        list_letters.append(let[1][0])
    list_letters = set(list_letters)
    list_letters = list(list_letters)
    list_letters.sort()
    return list_letters


print(thesaurus('Иван', 'Марина', 'Пётр', 'Саня', 'Илья', 'Паша', 'Марина'))
print(thesaurus_adv('Илья Пшеничников', 'Кто-то Второй'))
