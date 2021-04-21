# Задание 3

from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

klass_tutor = ((tutor, klass) for tutor, klass in zip_longest(tutors, klasses) if tutor)
print(type(klass_tutor))
for el in klass_tutor:
    print(el)

# print(next(klass_tutor))


# def klass_tutor_gen():
#     for tutor, klass in zip_longest(TUTORS, KLASSES):
#         if tutor is None:
#             break
#         yield tutor, klass
#
#
# klass_tutor = klass_tutor_gen()
# for el in klass_tutor:
#     print(el)
