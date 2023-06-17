import json
import struct


code = './compile/code.py'
info = './compile/info.json'
output = r'C:\Users\Fluorum\PycharmProjects\GigaChat\client\mods\ms-audio'

f_code = open(code, 'r')
f_info = open(info, 'r')
f_output = open(f'{output}.h4gc', 'wb+')

code = f_code.read().encode()
info = json.dumps(json.load(f_info)).encode()

del output

f_output.write(struct.pack('I', len(info)) + info + struct.pack('I', len(code)) + code)
