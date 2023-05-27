import json
import zipfile
import zipimport
import os


modules = {}


def get_mods():

    directory = "./mods/"

    files = []

    for file in os.listdir(directory):

        if file.endswith(".h4gc"):

            files.append(file)

    return files


for file in get_mods():

    modules[file[:-5]] = {'file': zipimport.zipimporter(f'./mods/{file}')}

    modules[file[:-5]]['module'] = modules[file[:-5]]['file'].load_module('main')

    with zipfile.ZipFile(f'./mods/{file}', 'r') as arch:

        with arch.open('info.json') as info:

            modules[file[:-5]]['info'] = json.load(info)


# print(modules)


def call(module, packet):

    return eval(f"modules['{module}']['module'].main({packet})")
