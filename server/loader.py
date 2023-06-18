import glob
import os


def properties_loader(file_path):
    parsed_data = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()  # Удаляем лишние пробелы и символы перевода строки
            if line:  # Пропускаем пустые строки
                key_value = line.split('=')
                if len(key_value) == 2:  # Проверяем, что строка содержит ключ и значение
                    key, value = key_value
                    key = key.strip()
                    value = value.strip()

                    if '[' in key and ']' in key:  # Проверяем, есть ли указание типа значения в ключе
                        key, value_type = key.split('[')
                        value_type = value_type[:-1]  # Удаляем закрывающую скобку ']'

                        if value_type == 'int':
                            value = int(value)
                        elif value_type == 'tuple':
                            value = tuple(value.split(', '))

                    parsed_data[key] = value

    return parsed_data


def get_files():
    mods = []

    for file_path in glob.glob('./mods/*.h4gc'):
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        mods.append(file_name)

    return mods


