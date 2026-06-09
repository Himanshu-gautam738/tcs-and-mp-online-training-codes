from cryptography.fernet import Fernet
import hashlib

# Encryption
key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt_data(data):
    return cipher.encrypt(data.encode())

def decrypt_data(enc):
    return cipher.decrypt(enc).decode()

# Hashing
def hash_data(data):
    return hashlib.sha256(data.encode()).hexdigest()

# Access Control
users = {
    "admin": "full",
    "user": "read",
    "guest": "none"
}

def check_access(username, action):
    role = users.get(username)
    if role == "full":
        return "Access Granted"
    elif role == "read" and action == "read":
        return "Access Granted"
    else:
        return "Access Denied"

# Simulation
data = "Sensitive Data"

enc = encrypt_data(data)
print("Encrypted:", enc)

dec = decrypt_data(enc)
print("Decrypted:", dec)

hashed = hash_data(data)
print("Hash:", hashed)

print(check_access("admin", "write"))
print(check_access("user", "read"))
print(check_access("guest", "write"))