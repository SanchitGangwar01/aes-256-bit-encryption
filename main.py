import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image
from aes_logic import *  # This imports the AES functions (encrypt_file, decrypt_file, etc.)

class AESApp:
    def __init__(self, app):
        self.app = app
        self.app.geometry("600x600")
        self.app.resizable(0, 0)
        self.app.title("AES-256 Encryptor/Decryptor")

        # Load images for the sidebar and button icons
        side_img_data = Image.open("images.jpeg")
        aes_encrypt_icon_data = Image.open("img2.png")

        side_img = ctk.CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(300, 600))
        img1_icon = ctk.CTkImage(dark_image=aes_encrypt_icon_data, light_image=aes_encrypt_icon_data, size=(20, 20))

        # Sidebar image
        ctk.CTkLabel(master=app, text="", image=side_img).pack(expand=True, side="left")

        # Frame for controls
        frame = ctk.CTkFrame(master=app, width=300, height=600, fg_color="#ffffff")
        frame.pack_propagate(0)
        frame.pack(expand=True, side="right")

        # Header text
        ctk.CTkLabel(master=frame, text="AES encryption and Decryption", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 15)).pack(anchor="w", pady=(50, 5), padx=(25, 0))
        ctk.CTkLabel(master=frame, text="Made by Sanchit Gangwar", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 12)).pack(anchor="w", padx=(25, 0))

        # Key entry
        ctk.CTkLabel(master=frame, text="  Enter Key(32 bytes):", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), image=img1_icon, compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
        self.key_entry = ctk.CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000")
        self.key_entry.pack(anchor="w", padx=(25, 0))

        # Generate Random Key Button
        self.generate_key_btn = ctk.CTkButton(master=frame, text="Generate Random Key", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", width=225, command=self.generate_random_key)
        self.generate_key_btn.pack(anchor="w", pady=(10, 0), padx=(25, 0))

        # Combined Buttons for encrypting and decrypting files
        self.encrypt_documents_btn = ctk.CTkButton(master=frame, text="Encrypt Document Files (Pdf/Txt)", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", width=225, command=self.encrypt_documents)
        self.encrypt_documents_btn.pack(anchor="w", pady=(25, 0), padx=(25, 0))

        self.decrypt_documents_btn = ctk.CTkButton(master=frame, text="Decrypt Document Files", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", width=225, command=self.decrypt_documents)
        self.decrypt_documents_btn.pack(anchor="w", pady=(25, 0), padx=(25, 0))

        self.encrypt_media_btn = ctk.CTkButton(master=frame, text="Encrypt Media Files (Image/Video)", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", width=225, command=self.encrypt_media)
        self.encrypt_media_btn.pack(anchor="w", pady=(25, 0), padx=(25, 0))

        self.decrypt_media_btn = ctk.CTkButton(master=frame, text="Decrypt Media Files", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", width=225, command=self.decrypt_media)
        self.decrypt_media_btn.pack(anchor="w", pady=(25, 0), padx=(25, 0))


    def generate_random_key(self):
     #logic for generating the random key
      return
    def get_validated_key(self):
     # logic for validating the key
     return
       

    def encrypt_documents(self):
      return
    def decrypt_documents(self):
     return

    def encrypt_media(self):
     return
    def decrypt_media(self):
      return

if __name__ == "__main__":
    app = ctk.CTk()
    AESApp(app)
    app.mainloop()
