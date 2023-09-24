from cryptography.fernet import Fernet


class hide:
    def encode_message(message1):
        fernet = Fernet(b'K4UptMTVmGCYMzeV_MA0TZIQ52FgPOnoyvMkJ0bPF3w=')
        encMessage = fernet.encrypt(message1.encode())
        return encMessage

    def decode_message(message1):
        message1 = bytes(message1,'utf-8')
        fernet = Fernet(b'K4UptMTVmGCYMzeV_MA0TZIQ52FgPOnoyvMkJ0bPF3w=')
        decMessage = fernet.decrypt(message1).decode()
        return decMessage
