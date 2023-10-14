def caesar_encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift + key) % 26 + shift)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, key):
    return caesar_encrypt(text, -key)