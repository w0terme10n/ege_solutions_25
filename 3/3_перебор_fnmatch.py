from fnmatch import fnmatch


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


# список, куда поместим будущие числа под ответ
nums = []

# начинаем перебор
for n in range(590306, 10**8 + 1):
    # проверка на маску
    if fnmatch(str(n), '5*9?3?6'):
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