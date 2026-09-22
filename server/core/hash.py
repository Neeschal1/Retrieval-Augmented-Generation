from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()

def create_hashed_data(password: str):
    return password_hash.hash(password)

def compare_data(plainPassword: str, hashedPassword: str):
    return password_hash.verify(plainPassword, hashedPassword)