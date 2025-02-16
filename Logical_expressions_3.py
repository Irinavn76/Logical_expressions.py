age = input('Вы совершеннолетний (Да/Нет): ')
citizen = input('Вы гражданин страны (Да/Нет): ')
judge = input('Вы cудимы (Да/Нет): ')
yes_choice = 'Да'.lower()
no_choice = 'Нет'.lower()

if age == yes_choice and citizen == yes_choice and judge == no_choice :
    print("Вы можете голосовать!")
else:
    print("Вы не можете голосовать!")