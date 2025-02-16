user_input_1 = input('Вы совершеннолетний (да/нет): ')
user_input_2 = input('Вы гражданин страны (да/нет): ')
user_input_3 = input('Вы cудимы (да/нет): ')
yes_choice = 'да'
no_choice = 'нет'

if user_input_1 == yes_choice and user_input_2 == yes_choice and user_input_3 == no_choice :
    print("Вы можете голосовать!")
else:
    print("Вы не можете голосовать!")