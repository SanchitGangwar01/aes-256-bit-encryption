import os
import secrets
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from PIL import Image
import cv


# Function to ensure the key is exactly 32 bytes long
def ensure_32_byte_key(key):
    if isinstance(key, str):
        key = bytes.fromhex(key)  # Convert the hex string to bytes

    if len(key) < 32:
        key = key.ljust(32, b'\0')  # Pad the key if too short
    elif len(key) > 32:
        key = key[:32]  # Truncate the key if too long
    
    return key


# Function to generate a random 32-byte key
def generate_random_key():
    key = secrets.token_bytes(32)  # 32-byte key for AES-256
    return key.hex()


# General encryption function for both documents and media
def encrypt_file(key, file_path, file_type="document"):
    try:
        key = ensure_32_byte_key(key)

        # Generate a random IV
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

        with open(file_path, 'rb') as file:
            data = file.read()

        # Pad the data to block size
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_data = padder.update(data) + padder.finalize()

        # Encrypt the data
        encryptor = cipher.encryptor()
        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

        # Save the encrypted data with IV
        encrypted_file_path = file_path + ".enc"
        with open(encrypted_file_path, 'wb') as encrypted_file:
            encrypted_file.write(iv + encrypted_data)

        return encrypted_file_path
    except Exception as e:
        return f"Error: {str(e)}"


# General decryption function for both documents and media
def decrypt_file(key, file_path, file_type="document"):
    try:
        key = ensure_32_byte_key(key)

        # Open encrypted file
        with open(file_path, 'rb') as encrypted_file:
            data = encrypted_file.read()

        # Extract the IV and encrypted data
        iv = data[:16]
        encrypted_data = data[16:]

        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

        # Decrypt the data
        decryptor = cipher.decryptor()
        decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

        # Unpad the decrypted data
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()

        # Save the decrypted data
        decrypted_file_path = file_path[:-4]  # Remove the .enc extension
        with open(decrypted_file_path, 'wb') as decrypted_file:
            decrypted_file.write(unpadded_data)

        return decrypted_file_path
    except Exception as e:
        return f"Error: {str(e)}"


# Encrypting document files (PDF, TXT, DOC)
def encrypt_document(key, file_path):
    return encrypt_file(key, file_path, file_type="document")


# Decrypting document files
def decrypt_document(key, file_path):
    return decrypt_file(key, file_path, file_type="document")


# Encrypting media files (Images, Videos)
def encrypt_media(key, file_path):
    return encrypt_file(key, file_path, file_type="media")


# Decrypting media files
def decrypt_media(key, file_path):
    return decrypt_file(key, file_path, file_type="media")


# Encrypting images
def encrypt_image(key, file_path):
    return encrypt_media(key, file_path)


# Decrypting images
def decrypt_image(key, file_path):
    return decrypt_media(key, file_path)


# Encrypting video files
def encrypt_video(key, file_path):
    return encrypt_media(key, file_path)


# Decrypting video files
def decrypt_video(key, file_path):
    return decrypt_media(key, file_path)
