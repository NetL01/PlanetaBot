import telebot
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes
from base64 import b64encode, b64decode

from config import bot

# gen open and close RSA
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()

# PEM
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# save keys
with open("private_key.pem", "wb") as f:
    f.write(private_pem)
with open("public_key.pem", "wb") as f:
    f.write(public_pem)

def encrypt_message(message, public_key):
    encrypted_message = public_key.encrypt(
        message.encode('utf-8'),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return b64encode(encrypted_message).decode('utf-8')

def decrypt_message(encrypted_message, private_key):
    decrypted_message = private_key.decrypt(
        b64decode(encrypted_message),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted_message.decode('utf-8')


def go_encode(message):
    try:
        plaintext = message.text.split(' ', 1)[1]
        encrypted_text = encrypt_message(plaintext, public_key)
        bot.reply_to(message, f"Зашифрованное сообщение: `{encrypted_text}`", parse_mode='MarkDown')
    except Exception as e:
        bot.reply_to(message, "Ошибка при шифровании сообщения.")

def go_decode(message):
    try:
        ciphertext = message.text.split(' ', 1)[1]
        decrypted_text = decrypt_message(ciphertext, private_key)
        bot.reply_to(message, f"Расшифрованное сообщение: `{decrypted_text}`", parse_mode='MarkDown')
    except Exception as e:
        bot.reply_to(message, "Ошибка при дешифровании сообщения.")