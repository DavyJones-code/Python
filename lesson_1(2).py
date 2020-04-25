sec = int(input('Введите время в секундах: '))
hour = int(sec / 3600)
min = int(sec - hour * 3600) // 60
sec_original = int(sec - hour * 3600 - min * 60)
print(f'{hour} : {min} : {sec_original}')
