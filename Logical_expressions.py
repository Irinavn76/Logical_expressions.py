age = int(input('Введите ваш возраст: '))
country = str(input('Введите страну гражданства: '))
status = str(input('Введите судим или не судим: '))

is_russian = country == 'Россия'  # Сравниваем введенную страну с "Россия"
is_not_judge = status == 'не судим'  # Проверяем статус судимости

if age >=18 and is_russian and is_not_judge :
    print("Вы можете голосовать!")

else:
    print("Вы не можете голосовать!")
