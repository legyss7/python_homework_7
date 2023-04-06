# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко
# он их придумывает, Вам стоит написать программу. Винни-Пух считает, что
# ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе
# стихотворения одинаковое. Фраза может состоять из одного слова, если во
# фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с
# клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в
# порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
# **Вывод:** Парам пам-пам


def string_count_vowels(string):
    list_phrase = string.split(' ')
    list_symbol = list()
    vowels = ['а', 'о', 'и', 'ы', 'у', 'э']
    count = 0
    count_vowels_phrase = []
    for i in range(len(list_phrase)):
        list_symbol = list(list_phrase[i])
        count = 0
        for j in range(len(list_symbol)):
            for k in range(len(vowels)):
                if list_symbol[j] == vowels[k]:
                    count += 1
        count_vowels_phrase.append(count)
    return count_vowels_phrase


def rhythm(count_vowels):
    for i in range(1, len(count_vowels)):
        if count_vowels[0] != count_vowels[i]:
            return 'Пам парам'
    return 'Парам пам-пам'


list_string = 'пара-ра-рам рам-пам-папам па-ра-па-да'
# list_string = input('Введите стихотворение: ')
print(list_string)
print(rhythm(string_count_vowels(list_string)))