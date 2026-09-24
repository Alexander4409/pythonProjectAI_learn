import math

power = int(input('Введите мощность алфавита:'))
length = int(input('Введите количество символов в пароле:'))
count = int(input('Введите количество паролей:'))
bits_symbol = math.cail(math.log2 (power))
bits_password = bits_symbol * length
bits_password = math.ceil( bits_password / 8)
total_bits = bits_password * count
print(f"Общий обьём памяти: {total_bits} байт")
