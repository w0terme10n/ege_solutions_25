# импорт функции для генерации комбинаций
from itertools import product


# функция для вычисления делителей числа number
def divs(number):
    # список куда поместим делители
    d = []
    # перебор делителей до корня из числа для оптимизации
    for i in range(1, int(number**0.5) + 1):
        if number % i == 0:
            d.append(i)
            # добавить остающиеся делители числа
            if i != number // i:
                d.append(number // i)
    return d


numbers = '0123456789'

# вычисление значений для "звездочки"
i1_values = ['']
# комбинации типа 0, 1, 2, 3 и т.д.
i1_values += list(numbers)
# комбинации типа 00, 01, 02, 03 и т.д.
i1_values += [''.join(i) for i in product(numbers, repeat=2)]


# список, куда поместим будущие числа под ответ
nums = []

# начинаем перебор
for i1 in i1_values:
    for i2 in numbers:
        for i3 in numbers:
            # составим по маске число
            n = int(f'5{i1}9{i2}3{i3}6')
            # находим делители числа
            d = divs(n)
            if len(d) == 20:
                # находим максимальный нечетный делитель числа
                max_odd_div = max([int(i) for i in d if i % 2 != 0])
                # проверка этого делителя на простоту
                if len(divs(max_odd_div)) == 2:
                    # добавляем в ответ
                    nums.append([n, sum(d) % n])

# сортировка в порядке убывания
nums.sort(reverse=True)
# вывод итогового ответа
for i in nums:
    print(*i)