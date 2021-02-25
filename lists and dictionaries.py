#Создаём переменные со стуктурой account типа словарь
account1 = {'login': 'ivan', 'password': 'q1'}
account2 = {'login': 'petr', 'password': 'q2'} 
account3 = {'login': 'olga', 'password': 'q3'}
account4 = {'login': 'anna', 'password': 'q4'}

#Создаём переменные со структурой user типа словарь 
user1 = {'name': 'Иван', 'age': 20, 'account': account1}
user2 = {'name': 'Петр', 'age': 25, 'account': account2}
user3 = {'name': 'Ольга', 'age': 18, 'account': account3}
user4 = {'name': 'Анна', 'age': 27, 'account': account4}

user_list = [user1, user2, user3, user4] #Создаём список user_list

#Первая часть программы
key = input('Введите ключ: ')  #Запрашиваем ключ

if key.lower() == 'name':  #Сравнваем с правильным  
    print(f'''значение ключа name для юзера 1 = {user1['name']}
значение ключа name для юзера 2 = {user2['name']}
значение ключа name для юзера 3 = {user3['name']}
значение ключа name для юзера 4 = {user4['name']}''')
else:
    print('Введённый ключ не найден.')

#Вторая часть
number = int(input('Введите порядковый номер пользователя: '))

#Сравниваем со значениями
if number == 1:
    print(f'''Данные по юзеру № 1
    Имя: {user1['name']}
    Возвраст: {user1['age']}
    Аккаунт: {account1['login']}
    Пароль: {account1['password']}''')
elif number == 2:
    print(f'''Данные по юзеру № 2
    Имя: {user2['name']}
    Возвраст: {user2['age']}
    Аккаунт: {account2['login']}
    Пароль: {account2['password']}''')
elif number == 3:
    print(f'''Данные по юзеру № 3
    Имя: {user3['name']}
    Возвраст: {user3['age']}
    Аккаунт: {account3['login']}
    Пароль: {account3['password']}''')
elif number == 4:
    print(f'''Данные по юзеру № 4
    Имя: {user4['name']}
    Возвраст: {user4['age']}
    Аккаунт: {account4['login']}
    Пароль: {account4['password']}''')
else:  #В случае не правильного значения
    print('Пользователь с указанным номером не найден.')

#Третья часть
user = input('Введите номер пользователя, которого нужно переместить в конец: ')

#Сравниваем со значениями
if user == 'user1':
    print(user_list)
    user1_1 = user_list.pop(0)
    user_list.append(user1_1)
    print(user_list)
elif user == 'user2':
    print(user_list)
    user2_1 = user_list.pop(1)
    user_list.append(user2_1)
    print(user_list)
elif user == 'user3':
    print(user_list)
    user3_1 = user_list.pop(2)
    user_list.append(user3_1)
    print(user_list)
elif user == 'user4':
    print(user_list)
    user4_1 = user_list.pop(3)
    user_list.append(user4_1)
    print(user_list)
else:
    print('Этот пользователь не найден.')

#Четвертая часть

middle_age1 = user1['age'] + user2['age'] + user3['age'] + user4['age']
middle_age = middle_age1/4
print('Средний возвраст пользователей: ', middle_age) 