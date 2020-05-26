from cryptography.fernet import Fernet

# Decrypt Gmail/Linkedin throwaway username/passwords
def decrypt_credentials():
    with open('username.key', 'rb') as f:
        key_username = Fernet(f.read())
        f.close()

    with open('username.encrypted', 'rb') as f:
        username_decrypted = key_username.decrypt(f.read())
        username = username_decrypted.decode('utf-8')
        f.close()

    with open('password.key', 'rb') as f:
        key_password = Fernet(f.read())
        f.close()

    with open('password.encrypted', 'rb') as f:
        password_decrypted = key_password.decrypt(f.read())
        password = password_decrypted.decode('utf-8')
        f.close()

    return username, password