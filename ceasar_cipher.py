def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - ord('а') + shift) % 33 + ord('а'))
            else:
                result += chr((ord(char) - ord('А') + shift) % 33 + ord('А'))
        else:
            result += char
    return result

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)


