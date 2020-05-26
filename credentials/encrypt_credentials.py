from cryptography.fernet import Fernet
import sys

# TODO: set up flag parsing
credentials = {
    'username' : sys.argv[1],
    'password' : sys.argv[2]
}

for cred in credentials:

    # Generate key
    key = Fernet.generate_key()
    f = Fernet(key)

    # Encrypt username
    cred_bytes = credentials[cred].encode()  # encode string to bytes
    cred_encrypted = f.encrypt(cred_bytes)

    # Store encrypted credential
    with open('{0}.encrypted'.format(cred), 'wb') as file_encrypted:
        file_encrypted.write(cred_encrypted)
        file_encrypted.close()

    # Store key
    with open('{0}.key'.format(cred), 'wb') as file_key:
        file_key.write(key)
        file_key.close()