def custom_write(file_name, strings):
    strings_pos = {}                                                                                                    # Создание функции custom_write (file_name, strings)
    with open(file_name, 'w', encoding='utf-8') as file:                                                                # file_name - название файла для записи
        for i, string in enumerate(strings, start=1):                                                                   # strings - список строк для записи
            position = file.tell()
            file.write(string + '\n')                                                                                   # Получение номера байта начала строки
            strings_pos[(i, position)] = string                                                                         # используем метод tell() перед записью
    return strings_pos

#Пример выполняемого кода из задания
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
# Вывод на консоль:
result = custom_write('text.txt', info)
for elem in result.items():
  print(elem)
