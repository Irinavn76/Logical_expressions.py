age = input('Вы совершеннолетний (Да/Нет): ')
citizen = input('Вы гражданин страны (Да/Нет): ')
judge = input('Вы cудимы (Да/Нет): ')


if age == 'Да'.lower() and citizen == 'Да'.lower() and judge == 'Нет'.lower() :
    print("Вы можете голосовать!")
else:
    print("Вы не можете голосовать!")