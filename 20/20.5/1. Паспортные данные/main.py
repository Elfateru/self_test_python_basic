data = {
    (5000, 123456): ('Иванов', 'Василий'),
    (6000, 111111): ('Иванов', 'Петр'),
    (7000, 222222): ('Медведев', 'Алексей'),
    (8000, 333333): ('Алексеев', 'Георгий'),
    (9000, 444444): ('Георгиева', 'Мария')
}

series = int(input('Введите серию паспорта: '))
number = int(input('Введите номер паспорта: '))

number_and_series = (series, number)

if number_and_series in data:
    print(data[number_and_series])
else:
    print('Такого человека нет')