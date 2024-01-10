# импорт функции для генерации комбинаций
from itertools import product


numbers = '0123456789'

# вычисление значений для "звездочки"
i2_values = ['']
# комбинации типа 0, 1, 2, 3 и т.д.
i2_values += list(numbers)
# комбинации типа 00, 01, 02, 03 и т.д.
i2_values += [''.join(i) for i in product(numbers, repeat=2)]

# список, куда поместим будущие числа под ответ
nums = []

# начинаем перебор
for i1 in numbers:
    for i2 in i2_values:
        for i3 in numbers:
            # составим по маске число
            n = int(f'2{i1}28{i2}0{i3}')
            if n % 1703 == 1526:
                nums.append(n)

# сортировка в порядке убывания
nums.sort(reverse=True)
# вывод итогового ответа
for n in nums:
    print(n, n // 1526)