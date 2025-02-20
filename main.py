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
        random_key = generate_random_key()  # This generates a hex string
        self.key_entry.delete(0, 'end')
        self.key_entry.insert(0, random_key)  # Show the hex string as it is
        messagebox.showinfo("Random Key Generated", f"Generated Key: {random_key}")


    def get_validated_key(self):      
        key = self.key_entry.get()
        # Check if the key is in hex format and convert it
        try:
            key_bytes = bytes.fromhex(key)
        except ValueError:
            # If it is not hex, we check if it's already 32 bytes long
            if len(key) != 32:
                messagebox.showerror("Error", "Key must be 32 bytes long (not hex).")
                self.key_entry.focus()  # Ensure focus stays on the key entry
                return None
            key_bytes = key.encode('utf-8')  # Convert string to bytes
        
        # Ensure the key is exactly 32 bytes long
        if len(key_bytes) != 32:
            messagebox.showerror("Error", "Key must be 32 bytes long.")
            self.key_entry.focus()  # Ensure focus stays on the key entry

            return None
        return key_bytes
     
     
    def encrypt_documents(self):
       key_bytes = self.get_validated_key()
       if not key_bytes:
            return

       file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("PDF files", "*.pdf")])
       if file_path:
            if file_path.endswith('.txt'):
                encrypted_file = encrypt_document(key_bytes, file_path)  # Calling the correct AES function for documents
            elif file_path.endswith('.pdf'):
                encrypted_file = encrypt_document(key_bytes, file_path)  # Same as above
            else:
                messagebox.showerror("Error", "Unsupported file type.")
                return
            messagebox.showinfo("Success", f"File encrypted successfully!\nEncrypted file: {encrypted_file}")

    def decrypt_documents(self):
       key_bytes = self.get_validated_key()
       if not key_bytes:
            return

       file_path = filedialog.askopenfilename(filetypes=[("Encrypted text files", "*.enc"), ("Encrypted PDFs", "*.enc")])
       if file_path:
            if file_path.endswith('.txt.enc'):
                decrypted_file = decrypt_document(key_bytes, file_path)  # Calling the correct AES function for documents
            elif file_path.endswith('.pdf.enc'):
                decrypted_file = decrypt_document(key_bytes, file_path)  # Same as above
            else:
                messagebox.showerror("Error", "Unsupported file type.")
                return
            messagebox.showinfo("Success", f"File decrypted successfully!\nDecrypted file: {decrypted_file}")

    def encrypt_media(self):
       key_bytes = self.get_validated_key()
       if not key_bytes:
            return

       file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif"), ("Video files", "*.mp4;*.avi;*.mkv")])
       if file_path:
            if file_path.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                encrypted_file = encrypt_media(key_bytes, file_path)  # Calling the correct AES function for media
            elif file_path.endswith(('.mp4', '.avi', '.mkv')):
                encrypted_file = encrypt_media(key_bytes, file_path)  # Same function for videos
            else:
                messagebox.showerror("Error", "Unsupported media type.")
                return
            messagebox.showinfo("Success", f"Media encrypted successfully!\nEncrypted file: {encrypted_file}")
   
   
    def decrypt_media(self):
        key_bytes = self.get_validated_key()
        if not key_bytes:
            return

        file_path = filedialog.askopenfilename(filetypes=[("Encrypted media files", "*.enc")])
        if file_path:
            decrypted_file = decrypt_media(key_bytes, file_path)  # Calling the correct AES function for media
            messagebox.showinfo("Success", f"Media decrypted successfully!\nDecrypted file: {decrypted_file}")


if __name__ == "__main__":
    app = ctk.CTk()
    AESApp(app)
    app.mainloop()
