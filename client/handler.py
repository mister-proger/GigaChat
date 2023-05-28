import json
import zipfile
import zipimport
import os


print('Загрузка хандлера')

modules = {}


def get_mods():

    directory = "./mods/"

    files = []

    for file in os.listdir(directory):

        if file.endswith(".h4gc"):

            files.append(file)

    return files


for file in get_mods():

    name = file[:-5]

    modules[name] = {'file': zipimport.zipimporter(f'./mods/{file}')}

    modules[name]['module'] = modules[name]['file'].load_module('main')

    with zipfile.ZipFile(f'./mods/{file}', 'r') as arch:

        with arch.open('info.json') as info:

            modules[name]['info'] = json.load(info)


del name


def call(module, packet):

    return eval(f"modules['{module}']['module'].main({packet})")


print('Загрузка хандлера завершена')
