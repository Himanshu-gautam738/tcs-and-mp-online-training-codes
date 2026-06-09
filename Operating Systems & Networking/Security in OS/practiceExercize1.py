from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Firewall
def firewall(packet):
    blocked_ports = [23, 25]
    if packet["port"] in blocked_ports:
        return "Blocked"
    return "Allowed"

# Encryption
def encrypt_data(data, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(data.encode(), AES.block_size))
    return cipher.iv, ciphertext

def decrypt_data(iv, ciphertext, key):
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    return unpad(cipher.decrypt(ciphertext), AES.block_size).decode()

# Intrusion Detection
def intrusion_detection(logs):
    for log in logs:
        if "failed" in log.lower():
            print("Alert: Suspicious activity detected ->", log)

# Simulation
packet = {"ip": "192.168.1.5", "port": 23}
print("Firewall:", firewall(packet))

key = get_random_bytes(16)
iv, encrypted = encrypt_data("Hello Secure World", key)
print("Encrypted:", encrypted)

decrypted = decrypt_data(iv, encrypted, key)
print("Decrypted:", decrypted)

logs = ["Login success", "Failed login attempt", "Access granted"]
intrusion_detection(logs)