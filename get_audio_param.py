import pyaudio

p = pyaudio.PyAudio()

device_count = p.get_device_count()

for i in range(device_count):
    device_info = p.get_device_info_by_index(i)
    device_name = device_info['name']
    print(device_info)
    print()
    # print(f"Device Index: {i}")
    # print(f"Device Name: {device_name}")
    # print(f"Device Host API: {device_info['hostApi']}")
    # print()
