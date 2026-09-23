from cryptography.fernet import Fernet
from env_config import Config

cipher = Fernet(Config.ENCRYPTION_KEY.encode())

def encrypt_data(data: str) -> str:
    encrypted = cipher.encrypt(data.encode())
    return encrypted.decode()

def decrypt_data(encrypted_data: str) -> str:
    decrypted = cipher.decrypt(encrypted_data.encode())
    return decrypted.decode()