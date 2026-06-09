from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad, unpad

password = b"mypassword"
salt = get_random_bytes(16)

key = PBKDF2(password, salt, dkLen=32)

cipher = AES.new(key, AES.MODE_CBC)
plaintext = b"Hello, Security!"

ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

print("Encrypted:", ciphertext)

cipher_dec = AES.new(key, AES.MODE_CBC, iv=cipher.iv)
decrypted = unpad(cipher_dec.decrypt(ciphertext), AES.block_size)

print("Decrypted:", decrypted.decode())