from cryptography.fernet import Fernet


class hide:
    def encode_message(message1):
        """
        Dont use in Production 
        its Public Key
        """
        fernet = Fernet(b'FVv3JlQzbaZJom2IH9NNAy0cDJy_Hv-b2J5DxfWRsXE=')
        encMessage = fernet.encrypt(message1.encode())
        return encMessage

    def decode_message(message1):
        """
        Dont use in Production 
        its Public Key
        """
        message1 = bytes(message1,'utf-8')
        fernet = Fernet(b'FVv3JlQzbaZJom2IH9NNAy0cDJy_Hv-b2J5DxfWRsXE=')
        decMessage = fernet.decrypt(message1).decode()
        return decMessage


