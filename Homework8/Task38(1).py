def read_csv(filename=(r'C:\Users\CastAway\Desktop\GITGB\HomeWorkPython\HomeWork\Homework8\phonebook.csv')):
    """Функция читает csv-файл и возвращает список списков - строк csv-файла."""
    with open(filename, 'r', encoding='utf-8') as file:
        data = []
        for line in file:
            data.append(line.strip('\n').split(','))
    return data


def display_all_records():
    """Функция выводит на печать содержание всего справочника в отформатированном виде."""
    data = read_csv()
    for row in data:
        print(
            f'Фамилия: {row[0]}\nИмя: {row[1]}\nНомер телефона: {row[2]}\nКомментарий: {row[3]}\n')


def find_last_name():
    """Функция запрашивает фамилию абонента, находит данные по этой фамилии и выводит их на печать."""
    last_name = input('Введите фамилию: ')
    data = read_csv()
    for row in data:
        if row[0] == last_name:
            print(
                f'Фамилия: {row[0]}\nИмя: {row[1]}\nНомер телефона: {row[2]}\nКомментарий: {row[3]}\n')


def find_phone_number():
    """Функция запрашивает телефон абонента, находит соответствующие данные и выводит на печать"""
    phone = input('Введите номер телефона: ')
    data = read_csv()
    for row in data:
        if row[2] == phone:
            print(
                f'Фамилия: {row[0]}\nИмя: {row[1]}\nНомер телефона: {row[2]}\nКомментарий: {row[3]}\n')


def add_data(filename='phonebook.csv'):
    """Функция дополняет телефонный справочник данными нового абонента."""
    with open(filename, 'a', encoding='utf-8') as file:
        info = input(
            'Введите данные абонента (фамилия, имя, номер, комментарий - через запятую): ').split(', ')

        file.write(','.join(info) + '\n')
        print('Данные записаны.')



number = 0
while number != '6':
    print('Введите число для операции со справочником:')
    print('1 - вывести весь справочник;\n2 - найти абонента по фамилии;\n'
          '3 - найти абонента по номеру телефона;\n4 - ввести данные нового абонента;\n6 - завершить работу.')

    number = input()

    if number == '1':
        display_all_records()

    elif number == '2':
        find_last_name()

    elif number == '3':
        find_phone_number()

    elif number == '4':
        add_data()

else:
    print('Работа завершена.')
