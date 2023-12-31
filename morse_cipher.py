def morse_encrypt(text, language='Английский'):
    if language == 'Русский':
        morse_code = {'А': '.-', 'Б': '-...', 'В': '.--', 'Г': '--.', 'Д': '-..', 'Е': '.', 'Ё': '.', 'Ж': '...-',
                      'З': '--..', 'И': '..', 'Й': '.---', 'К': '-.-', 'Л': '.-..', 'М': '--', 'Н': '-.', 'О': '---',
                      'П': '.--.', 'Р': '.-.', 'С': '...', 'Т': '-', 'У': '..-', 'Ф': '..-.', 'Х': '....', 'Ц': '-.-.',
                      'Ч': '---.', 'Ш': '----', 'Щ': '--.-', 'Ъ': '--.--', 'Ы': '-.--', 'Ь': '-..-', 'Э': '...-...',
                      'Ю': '..--', 'Я': '.-.-'}
    else:
        morse_code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                      'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                      'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                      'Y': '-.--', 'Z': '--..'}

    encrypted_text = ''
    for char in text.upper():
        if char in morse_code:
            encrypted_text += morse_code[char] + ' '
        elif char == ' ':
            encrypted_text += ' '
    return encrypted_text.strip()

# Для дешифрования Морзе используем общий словарь для английского и русского языка
def morse_decrypt(encrypted_text, language='Английский'):
    if language == 'Русский':
        morse_code = {'.-': 'A', '-...': 'Б', '.--': 'В', '--.': 'Г', '-..': 'Д', '.': 'Е', '.': 'Ё', '...-': 'Ж',
                      '--..': 'З', '..': 'И', '.---': 'Й', '-.-': 'К', '.-..': 'Л', '--': 'М', '-.': 'Н', '---': 'О',
                      '.--.': 'П', '.-.': 'Р', '...': 'С', '-': 'Т', '..-': 'У', '..-.': 'Ф', '....': 'Х', '-.-.': 'Ц',
                      '---.': 'Ч', '----': 'Ш', '--.-': 'Щ', '--.--': 'Ъ', '-.--': 'Ы', '-..-': 'Ь', '...-...': 'Э',
                      '..--': 'Ю', '.-.-': 'Я', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
                      '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9'}
    else:
        morse_code = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
                  '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
                  '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
                  '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
                  '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9'}

    decrypted_text = ''
    morse_chars = encrypted_text.split(' ')
    for char in morse_chars:
        if char in morse_code:
            decrypted_text += morse_code[char]
        elif char == ' ':
            decrypted_text += ' '
    return decrypted_text