def vigenere_encrypt(text, key, language='Английский'):
    if language == 'Русский':
        alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        key = key.upper()
    else:
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        key = key.upper()

    encrypted_text = ""
    key_length = len(key)
    for i in range(len(text)):
        char = text[i]
        if char.upper() in alphabet:
            shift = alphabet.index(char.upper())
            if char.islower():
                encrypted_char = alphabet[(shift + alphabet.index(key[i % key_length])) % len(alphabet)].lower()
            else:
                encrypted_char = alphabet[(shift + alphabet.index(key[i % key_length])) % len(alphabet)]
        else:
            encrypted_char = char
        encrypted_text += encrypted_char

    return encrypted_text

def vigenere_decrypt(encrypted_text, key, language='Английский'):
    if language == 'Русский':
        alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        key = key.upper()
    else:
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        key = key.upper()

    decrypted_text = ""
    key_length = len(key)
    for i in range(len(encrypted_text)):
        char = encrypted_text[i]
        if char.upper() in alphabet:
            shift = alphabet.index(char.upper())
            if char.islower():
                decrypted_char = alphabet[(shift - alphabet.index(key[i % key_length])) % len(alphabet)].lower()
            else:
                decrypted_char = alphabet[(shift - alphabet.index(key[i % key_length])) % len(alphabet)]
        else:
            decrypted_char = char
        decrypted_text += decrypted_char

    return decrypted_text