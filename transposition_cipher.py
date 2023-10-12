def transposition_encrypt(text, key):
    encrypted_text = [''] * key

    for col in range(key):
        pointer = col
        while pointer < len(text):
            encrypted_text[col] += text[pointer]
            pointer += key

    return ''.join(encrypted_text)

def transposition_decrypt(encrypted_text, key):
    num_of_cols = len(encrypted_text) // key
    num_of_rows = key

    num_of_shaded_boxes = (num_of_cols * num_of_rows) - len(encrypted_text)

    plaintext = [''] * num_of_cols

    col = 0
    row = 0

    for symbol in encrypted_text:
        plaintext[col] += symbol
        col += 1

        if (col == num_of_cols) or (col == num_of_cols - 1 and row >= num_of_rows - num_of_shaded_boxes):
            col = 0
            row += 1

    return ''.join(plaintext)