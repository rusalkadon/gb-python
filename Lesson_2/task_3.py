# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года относится
# месяц (зима, весна, лето, осень). Напишите решения через list и dict.
month = input('Введите номер месяца:')
if int(month)<=0 or int(month)>12:
    print('Неверное номер месяца')
elif int(month) > 2 and int(month) < 6:
    print ('Весна')
elif int(month) >5 and int(month) <9:
    print('Лето')
elif int(month) >8 and int(month) <12:
    print('Осень')
else:
    print('Зима')


