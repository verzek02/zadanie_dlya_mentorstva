kol = int(input('Сколько раз вы хотите ввести данные: '))

hours = []
minutes = []
seconds = []

for i in range(kol):
    while True:
        print('Формат введения (час:минута:секунда)')
        try:
            hour = int(input('Введите часы:'))
            minute = int(input('Введите минуты:'))
            sec = int(input('Введите секунды:'))

            if hour < 0 or hour > 23:
                print('Часы должны быть в диапазоне от 0 до 23!')
            elif minute < 0 or minute > 59:
                print('Минуты должны быть в диапазоне от 0 до 59!')
            elif sec < 0 or sec > 59:
                print('Секунды должны быть в диапазоне от 0 до 59!')
            else:
                print('Верные данные!')
                hours.append(hour)
                minutes.append(minute)
                seconds.append(sec)
                break
        except ValueError:
            print('Данные введены неправильно! Попробуйте еще раз.')
print('Часы:', hours, 'Минуты:', minutes, 'Секунды:', seconds)

