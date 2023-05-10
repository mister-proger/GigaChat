import base64

def encode_audio(audio):
    """Кодирует аудио в base64 и возвращает строку"""
    encoded_audio = base64.b64encode(audio).decode("utf-8")
    return encoded_audio

def decode_audio(encoded_audio):
    """Декодирует строку из base64 и восстанавливает аудио"""
    decoded_audio = base64.b64decode(encoded_audio.encode("utf-8"))
    return decoded_audio
