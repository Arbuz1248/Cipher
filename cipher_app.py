
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from vigenere_cipher import vigenere_encrypt, vigenere_decrypt
from morse_cipher import morse_encrypt, morse_decrypt
from substitution_cipher import substitution_encrypt, substitution_decrypt
from ceasar_cipher import caesar_encrypt, caesar_decrypt
class CipherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cipher App")


        self.tab_control = ttk.Notebook(root)
        self.vigenere_tab = ttk.Frame(self.tab_control)
        self.morse_tab = ttk.Frame(self.tab_control)
        self.substitution_tab = ttk.Frame(self.tab_control)
        self.caesar_tab = ttk.Frame(self.tab_control)
        self.about_tab = ttk.Frame(self.tab_control)

        self.tab_control.add(self.vigenere_tab, text="Виженер")
        self.tab_control.add(self.morse_tab, text="Морзе")
        self.tab_control.add(self.substitution_tab, text="Замены")
        self.tab_control.add(self.caesar_tab, text="Шифр Цезаря")
        self.tab_control.add(self.about_tab, text="о программе")

        self.tab_control.pack(expand=1, fill="both")

        self.vigenere_frame = ttk.Frame(self.vigenere_tab)
        self.vigenere_frame.pack()

        self.vigenere_label = ttk.Label(self.vigenere_frame, text="Vigenere Cipher")
        self.vigenere_label.pack()

        self.language_label = ttk.Label(self.vigenere_tab, text="Выберите язык:")
        self.language_label.pack()
        self.language_var = tk.StringVar()
        self.language_var.set("english")  # Устанавливаем английский язык по умолчанию
        self.language_dropdown = ttk.Combobox(self.vigenere_tab, textvariable=self.language_var,
                                              values=["english", "russian"])
        self.language_dropdown.pack()

        self.vigenere_text = tk.Text(self.vigenere_frame, height=5, width=40)
        self.vigenere_text.pack()

        self.vigenere_key_label = ttk.Label(self.vigenere_frame, text="Enter Key:")
        self.vigenere_key_label.pack()
        self.vigenere_key = tk.Entry(self.vigenere_frame)
        self.vigenere_key.pack()

        self.vigenere_encrypt_button = ttk.Button(self.vigenere_frame, text="Encrypt", command=self.encrypt_vigenere)
        self.vigenere_encrypt_button.pack()

        self.vigenere_decrypt_button = ttk.Button(self.vigenere_frame, text="Decrypt", command=self.decrypt_vigenere)
        self.vigenere_decrypt_button.pack()

        self.morse_frame = ttk.Frame(self.morse_tab)
        self.morse_frame.pack()

        self.morse_label = ttk.Label(self.morse_frame, text="Morse Cipher")
        self.morse_label.pack()

        self.language_label_morse = ttk.Label(self.morse_tab, text="Выберите язык:")
        self.language_label_morse.pack()
        self.language_var_morse = tk.StringVar()
        self.language_var_morse.set("english")  # Устанавливаем английский язык по умолчанию
        self.language_dropdown_morse = ttk.Combobox(self.morse_tab, textvariable=self.language_var_morse,
                                                    values=["english", "russian"])
        self.language_dropdown_morse.pack()


        self.morse_text = tk.Text(self.morse_frame, height=5, width=40)
        self.morse_text.pack()

        self.morse_encrypt_button = ttk.Button(self.morse_frame, text="Encrypt", command=self.encrypt_morse)
        self.morse_encrypt_button.pack()

        self.morse_decrypt_button = ttk.Button(self.morse_frame, text="Decrypt", command=self.decrypt_morse)
        self.morse_decrypt_button.pack()

        self.substitution_frame = ttk.Frame(self.substitution_tab)
        self.substitution_frame.pack()

        self.substitution_label = ttk.Label(self.substitution_frame, text="Substitution Cipher")
        self.substitution_label.pack()

        self.language_label_substitution = ttk.Label(self.substitution_tab, text="Выберите язык:")
        self.language_label_substitution.pack()
        self.language_var_substitution = tk.StringVar()
        self.language_var_substitution.set("english")  # Устанавливаем английский язык по умолчанию
        self.language_dropdown_substitution = ttk.Combobox(self.substitution_tab,
                                                           textvariable=self.language_var_substitution,
                                                           values=["english", "russian"])
        self.language_dropdown_substitution.pack()


        self.substitution_text = tk.Text(self.substitution_frame, height=5, width=40)
        self.substitution_text.pack()

        self.substitution_encrypt_button = ttk.Button(self.substitution_frame, text="Encrypt",
                                                      command=self.encrypt_substitution)
        self.substitution_encrypt_button.pack()

        self.substitution_decrypt_button = ttk.Button(self.substitution_frame, text="Decrypt",
                                                      command=self.decrypt_substitution)
        self.substitution_decrypt_button.pack()


        self.copyright_label = ttk.Label(root, text="© 2023 Вологодский колледж связи и информационных технологий. Смирнов Андрей. Все права защищены.", anchor="center")
        self.copyright_label.pack(side="bottom", fill="x")

        self.encrypted_text = tk.Text(self.substitution_tab, height=10, width=50)
        self.encrypted_text.pack()
        self.decrypted_text = tk.Text(self.substitution_tab, height=10, width=50)
        self.decrypted_text.pack()

        self.vigenere_encrypted_text = tk.Text(self.vigenere_tab, height=10, width=50)
        self.vigenere_encrypted_text.pack()
        self.vigenere_decrypted_text = tk.Text(self.vigenere_tab, height=10, width=50)
        self.vigenere_decrypted_text.pack()

        self.encrypted_morse_text = tk.Text(self.morse_tab, height=10, width=50)
        self.encrypted_morse_text.pack()
        self.decrypted_morse_text = tk.Text(self.morse_tab, height=10, width=50)
        self.decrypted_morse_text.pack()


        self.caesar_text_label = ttk.Label(self.caesar_tab, text="Введите текст:")
        self.caesar_text_label.pack()
        self.caesar_text = tk.Text(self.caesar_tab, height=5, width=50)
        self.caesar_text.pack()

        self.caesar_key_label = ttk.Label(self.caesar_tab, text="Введите ключ (сдвиг):")
        self.caesar_key_label.pack()
        self.caesar_key_entry = ttk.Entry(self.caesar_tab)
        self.caesar_key_entry.pack()

        self.caesar_encrypted_text_label = ttk.Label(self.caesar_tab, text="Зашифрованный текст:")
        self.caesar_encrypted_text_label.pack()
        self.caesar_encrypted_text = tk.Text(self.caesar_tab, height=5, width=50)
        self.caesar_encrypted_text.pack()

        self.caesar_decrypted_text_label = ttk.Label(self.caesar_tab, text="Дешифрованный текст:")
        self.caesar_decrypted_text_label.pack()
        self.caesar_decrypted_text = tk.Text(self.caesar_tab, height=5, width=50)
        self.caesar_decrypted_text.pack()

        # Добавляем кнопки для шифрования и дешифрования
        self.encrypt_caesar_button = ttk.Button(self.caesar_tab, text="Зашифровать", command=self.encrypt_caesar)
        self.encrypt_caesar_button.pack()
        self.decrypt_caesar_button = ttk.Button(self.caesar_tab, text="Дешифровать", command=self.decrypt_caesar)
        self.decrypt_caesar_button.pack()












        # Добавьте текст с описанием каждого шифра во вкладке "О программе"
        about_text = """
                Программа для шифрования и дешифрования текста поддерживает следующие шифры:

                1. Шифр Виженера: Позволяет шифровать и дешифровать текст с использованием ключевого слова.
                2. Шифр Морзе: Переводит текст в азбуку Морзе и обратно.
                3. Шифр Замены: Заменяет каждую букву в тексте на другую букву согласно заданному словарю.
                4. Шифр Транспонирования: Использует технику перестановки символов в тексте с заданным ключом.

                Автор: Смирнов Андрей Сергеевич
                """
        about_label = ttk.Label(self.about_tab, text=about_text, wraplength=400)
        about_label.pack()

    def encrypt_caesar(self):
        text = self.caesar_text.get("1.0", "end-1c")
        key = int(self.caesar_key_entry.get())

        encrypted_text = caesar_encrypt(text, key)

        # Очистите текстовые поля перед обновлением
        self.caesar_encrypted_text.delete(1.0, "end")
        self.caesar_decrypted_text.delete(1.0, "end")

        # Вставьте зашифрованный текст в соответствующее текстовое поле
        self.caesar_encrypted_text.insert("1.0", encrypted_text)

    def decrypt_caesar(self):
        text = self.caesar_text.get("1.0", "end-1c")
        key = int(self.caesar_key_entry.get())

        decrypted_text = caesar_decrypt(text, key)

        # Очистите текстовые поля перед обновлением
        self.caesar_encrypted_text.delete(1.0, "end")
        self.caesar_decrypted_text.delete(1.0, "end")

        # Вставьте дешифрованный текст в соответствующее текстовое поле
        self.caesar_decrypted_text.insert("1.0", decrypted_text)




        # Очистите текстовое поле перед обновлением
        self.decrypted_transposition_text.delete(1.0, "end")

        # Вставьте зашифрованный текст в текстовое поле
        self.decrypted_transposition_text.insert("1.0", decrypted_text)

    def encrypt_substitution(self):
        text = self.substitution_text.get("1.0", "end-1c")
        language = self.language_var_substitution.get()
        encrypted_text = substitution_encrypt(text, language)

        # Очистите текстовое поле перед обновлением
        self.encrypted_text.delete(1.0, "end")

        # Вставьте зашифрованный текст в текстовое поле
        self.encrypted_text.insert("1.0", encrypted_text)

    def decrypt_substitution(self):
        text = self.substitution_text.get("1.0", "end-1c")
        language = self.language_var_substitution.get()
        decrypted_text = substitution_decrypt(text, language)

        # Очистите текстовое поле перед обновлением
        self.decrypted_text.delete(1.0, "end")

        # Вставьте дешифрованный текст в текстовое поле
        self.decrypted_text.insert("1.0", decrypted_text)

    def encrypt_morse(self):
        text = self.morse_text.get("1.0", "end-1c")
        language = self.language_var_morse.get()
        encrypted_morse = morse_encrypt(text, language)

        # Очистите текстовое поле перед обновлением
        self.encrypted_morse_text.delete(1.0, "end")

        # Вставьте зашифрованный текст в текстовое поле
        self.encrypted_morse_text.insert("1.0", encrypted_morse)

    def decrypt_morse(self):
        morse_text = self.morse_text.get("1.0", "end-1c")
        decrypted_text = morse_decrypt(morse_text)

        # Очистите текстовое поле перед обновлением
        self.decrypted_morse_text.delete(1.0, "end")

        # Вставьте дешифрованный текст в текстовое поле
        self.decrypted_morse_text.insert("1.0", decrypted_text)








    def encrypt_vigenere(self):
        # Получите текст и ключ
        text = self.vigenere_text.get("1.0", "end-1c")
        key = self.vigenere_key.get()
        language = self.language_var.get()

        # Зашифруйте текст
        encrypted_text = vigenere_encrypt(text, key, language)

        # Очистите текстовые поля перед обновлением
        self.vigenere_encrypted_text.delete(1.0, "end")
        self.vigenere_decrypted_text.delete(1.0, "end")

        # Вставьте зашифрованный текст в текстовое поле
        self.vigenere_encrypted_text.insert("1.0", encrypted_text)

    def decrypt_vigenere(self):
        # Получите текст и ключ
        text = self.vigenere_text.get("1.0", "end-1c")
        key = self.vigenere_key.get()
        language = self.language_var.get()  # Получаем выбранный язы

        # Расшифруйте текст
        decrypted_text = vigenere_decrypt(text, key, language)

        # Очистите текстовые поля перед обновлением
        self.vigenere_encrypted_text.delete(1.0, "end")
        self.vigenere_decrypted_text.delete(1.0, "end")

        # Вставьте дешифрованный текст в текстовое поле
        self.vigenere_decrypted_text.insert("1.0", decrypted_text)



def main():
    root = tk.Tk()
    app = CipherApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()