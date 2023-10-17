from cryptography.fernet import Fernet


class hide:
    def encode_message(message1):
        fernet = Fernet(b'my_key')
        encMessage = fernet.encrypt(message1.encode())
        return encMessage

    def decode_message(message1):
        message1 = bytes(message1,'utf-8')
        fernet = Fernet(b'my_key')
        decMessage = fernet.decrypt(message1).decode()
        return decMessage
