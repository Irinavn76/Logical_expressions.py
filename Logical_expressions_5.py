age = input('Вы совершеннолетний (Да/Нет): ').lower()
citizen = input('Вы гражданин страны (Да/Нет): ').lower()
judge = input('Вы cудимы (Да/Нет): ').lower()


if age == 'да' and citizen == 'да' and judge == 'нет' :
    print("Вы можете голосовать!")
else:
    print("Вы не можете голосовать!")