import glob
import json
import os
import struct


def importer():

    mods = {}

    variable = {}

    def get_file_names():
        file_names = []

        for file_path in glob.glob('./mods/*.h4gc'):
            file_name = os.path.splitext(os.path.basename(file_path))[0]
            file_names.append(file_name)

        return file_names

    def import_code_from_file(file_path, variable_address):
        with open(file_path, 'rb') as file:
            data = file.read()
            len_a = struct.unpack('I', data[:4])[0]
            info = json.loads(data[4:4 + len_a])
            len_b = struct.unpack('I', data[4 + len_a:4 + len_a + 4])[0]
            code = data[4 + len_a + 4:4 + len_a + 4 + len_b]

        exec(code, variable_address)

        return info, variable_address['Main']

    for mod in get_file_names():

        mods[mod] = {}

        mods[mod]['info'], mods[mod]['code'] = import_code_from_file(f'./mods/{mod}.h4gc', variable)

    return mods


mods = importer()
print(mods)
