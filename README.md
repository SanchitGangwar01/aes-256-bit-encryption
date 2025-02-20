---
# AES-256 Encryptor/Decryptor

This Python application provides an easy-to-use graphical interface for encrypting and decrypting documents and media files using AES-256 encryption. Built using `customtkinter`, `Pillow`, and `cryptography` libraries, it allows users to securely encrypt and decrypt text, PDF, image, and video files with a 32-byte key.

## Features

- **Generate Random Key**: The application allows the generation of a random 32-byte key for AES-256 encryption.
- **File Encryption/Decryption**: 
  - **Documents**: Supports encrypting and decrypting `.txt` and `.pdf` files.
  - **Media**: Supports encrypting and decrypting media files such as `.png`, `.jpg`, `.jpeg`, `.bmp`, `.gif`, `.mp4`, `.avi`, and `.mkv`.
- **Secure AES-256**: Uses AES-256 encryption (CBC mode) with PKCS7 padding.
- **Cross-platform Support**: Can be run on any platform that supports Python (Windows, Linux, macOS).

## Installation

### Requirements

- Python 3.6 or higher
- Required Python libraries:
  - `cryptography`
  - `Pillow`
  - `customtkinter`
  - `opencv-python-headless` (for media encryption)

You can install the required dependencies using `pip`:

```bash
pip install cryptography Pillow customtkinter opencv-python-headless
```

## Usage

1. **Running the Application**:
   - Clone the repository or download the Python files to your local machine.
   - Run the `main.py` file using Python.

```bash
python main.py
```

2. **Main Features**:
   - **Enter Key**: Enter a 32-byte key manually or generate a random one.
   - **Encrypt/Decrypt Documents**: Choose from `.txt` or `.pdf` files for encryption or decryption.
   - **Encrypt/Decrypt Media**: Choose from image/video files for encryption or decryption.
   - **Key Format**: The key can either be in hexadecimal format (32 bytes) or a raw string format, which will be converted into bytes.

3. **File Encryption Process**:
   - Select a file for encryption.
   - Enter a 32-byte key (or generate a random key).
   - The application will encrypt the file and save it with a `.enc` extension.

4. **File Decryption Process**:
   - Select an encrypted file with the `.enc` extension.
   - Enter the same key used during encryption.
   - The application will decrypt the file and save it in the original format.

## File Structure

- `main.py`: The main graphical user interface (GUI) of the application built using `customtkinter`.
- `aes_logic.py`: Contains the core logic for AES encryption and decryption (handles file encryption and decryption, key generation).
- `images.jpeg`: Sidebar image used in the GUI.
- `img2.png`: Icon image used for buttons in the GUI.
- `screenshots/`: Folder containing screenshots of the application (to be uploaded as part of the project).

## AES-256 Encryption Logic

The AES-256 encryption logic is implemented using the `cryptography` library. The encryption process is done in **CBC mode** with **PKCS7 padding**. Files are read in binary mode, encrypted, and then saved with the `.enc` extension. Decryption is performed by reversing the process and unpadding the decrypted data.

### AES Key Handling:
- The key is automatically padded or truncated to ensure it is exactly 32 bytes long.
- The generated key can be used for both encryption and decryption processes.

### File Encryption and Decryption:
- **Encrypting Documents**: Encrypts text and PDF files.
- **Encrypting Media**: Encrypts image and video files.
- **Decrypting Documents and Media**: Decrypts any previously encrypted files (documents and media) with the same key used during encryption.

## Example

1. **Encrypt a Document**:
   - Click on "Encrypt Document Files (Pdf/Txt)".
   - Choose a `.txt` or `.pdf` file to encrypt.
   - Enter a 32-byte key or generate a random one.
   - The encrypted file will be saved with an `.enc` extension.

2. **Decrypt a Document**:
   - Click on "Decrypt Document Files".
   - Choose an encrypted `.txt.enc` or `.pdf.enc` file.
   - Enter the same key used for encryption.
   - The decrypted file will be saved in its original format.


## Credits

- **Author**: Sanchit Gangwar
- **Libraries Used**:
  - `cryptography` (for AES encryption/decryption)
  - `Pillow` (for image processing)
  - `customtkinter` (for the GUI)
  - `opencv-python-headless` (for media handling)

## Support

If you encounter any issues or have any questions, please feel free to open an issue in the GitHub repository, and I will try to respond as soon as possible.

---

### Screenshots

Here are some screenshots of the application in use:

- **Screenshot 1**: ![Alt Text](https://github.com/SanchitGangwar01/aes-256-bit-encryption/blob/main/screenshot1.png)
- **Screenshot 2**: ![Alt Text](https://github.com/SanchitGangwar01/aes-256-bit-encryption/blob/main/screenshot2.png)
- **Screenshot 3**: ![Alt Text](https://github.com/SanchitGangwar01/aes-256-bit-encryption/blob/main/screenshot3.png)

---
