letters = 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)

def encrypt(plaintext, key):
    ciphertext = ''
    for letter in plaintext:
        if letter.lower() in letters:
            index = letters.find(letter.lower())
            new_index = (index + key) % num_letters
            if letter.isupper():
                ciphertext += letters[new_index].upper()
            else:
                ciphertext += letters[new_index]
        else:
            ciphertext += letter
    return ciphertext

def decrypt(ciphertext, key):
    return encrypt(ciphertext, -key)

print('CAESAR CIPHER TASK 1')
print('Do you want to encrypt or decrypt?')
user_input = input('e/d: ').lower()

if user_input == 'e':
    print("ENCRYPTION MODE SELECTED")
    key = int(input("Enter the key: "))
    text = input('Enter the text to encrypt: ')
    ciphertext = encrypt(text, key)
    print(f'CIPHERTEXT: {ciphertext}')
elif user_input == 'd':
    print('DECRYPTION MODE SELECTED')
    key = int(input("Enter the key: "))
    text = input('Enter the text to decrypt: ')
    plaintext = decrypt(text, key)
    print(f'PLAINTEXT: {plaintext}')
