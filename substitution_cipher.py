substitution_key_english = {
    'A': 'X', 'B': 'Y', 'C': 'Z', 'D': 'A', 'E': 'B', 'F': 'C', 'G': 'D', 'H': 'E', 'I': 'F', 'J': 'G',
    'K': 'H', 'L': 'I', 'M': 'J', 'N': 'K', 'O': 'L', 'P': 'M', 'Q': 'N', 'R': 'O', 'S': 'P', 'T': 'Q',
    'U': 'R', 'V': 'S', 'W': 'T', 'X': 'U', 'Y': 'V', 'Z': 'W'
}

substitution_key_russian = {
    'А': 'X', 'Б': 'Y', 'В': 'Z', 'Г': 'A', 'Д': 'B', 'Е': 'C', 'Ё': 'C', 'Ж': 'D', 'З': 'E', 'И': 'F',
    'Й': 'G', 'К': 'H', 'Л': 'I', 'М': 'J', 'Н': 'K', 'О': 'L', 'П': 'M', 'Р': 'N', 'С': 'O', 'Т': 'P',
    'У': 'Q', 'Ф': 'R', 'Х': 'S', 'Ц': 'T', 'Ч': 'U', 'Ш': 'V', 'Щ': 'W', 'Ъ': 'X', 'Ы': 'Y', 'Ь': 'Z',
    'Э': ' ', 'Ю': ' ', 'Я': ' '
}

def substitution_encrypt(text, language='english'):
    if language == 'russian':
        substitution_key = substitution_key_russian
    else:
        substitution_key = substitution_key_english

    encrypted_text = ''.join(substitution_key.get(char, char) for char in text.upper())
    return encrypted_text

def substitution_decrypt(encrypted_text, language='english'):
    if language == 'russian':
        decryption_key = {v: k for k, v in substitution_key_russian.items()}
    else:
        decryption_key = {v: k for k, v in substitution_key_english.items()}

    decrypted_text = ''.join(decryption_key.get(char, char) for char in encrypted_text)
    return decrypted_text