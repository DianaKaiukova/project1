#Объявляем переменные

pwd = input('Введите пароль:')

pwd_long = len(pwd)



#Перебор исключений

try:

    result = 1/pwd_long

    result = int(pwd)

    print('Ваш пароль состоит только из цифр')

except ZeroDivisionError:

    print('Вы ввели пустой пароль')  

except ValueError:

    print('Требования к паролю соблюдены')

    