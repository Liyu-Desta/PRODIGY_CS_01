def encrypt(PlainText, shift_value):
    Cy_text = ""
    for i in PlainText:
        if i.isalpha():  # Check if the character is a letter
            if i.islower():
                Cy_text += chr((ord(i) - ord('a') + shift_value) % 26 + ord('a')) # shift each character by the value of shift_value for small letters
            elif i.isupper():
                Cy_text += chr((ord(i) - ord('A') + shift_value) % 26 + ord('A'))# shift each character by the value of shift_value for capital letters
        else:
            Cy_text += i  # Non-alphabet characters remain unchanged
    return Cy_text

def decrypt(cipherText, shift_value):
    Pl_Text = ""
    for i in cipherText:
        if i.isalpha():
            if i.islower():
                Pl_Text += chr((ord(i) - ord('a') - shift_value) % 26 + ord('a')) # shift each character back by the value of shift_value for small letters
            elif i.isupper():
                Pl_Text += chr((ord(i) - ord('A') - shift_value) % 26 + ord('A'))# shift each character back by the value of shift_value for capital letters
        else:
            Pl_Text += i
    return Pl_Text

def main():
    choice = input('What do you want to do with the text?\n1. Encrypt\n2. Decrypt\n')
    if choice == '1':
        PlainText = input("Provide your plain text please: ")
        shift_value = int(input("Provide your shift value please: "))
        print("Encrypted text:", encrypt(PlainText, shift_value))
    elif choice == '2':
        cipherText = input("Provide your cipher text please: ")
        shift_value = int(input("Provide your shift value please: "))
        print("Decrypted text:", decrypt(cipherText, shift_value))
    else:
        print("Invalid choice. Please enter 1 for encrypt or 2 for decrypt.")

if __name__ == "__main__":
    main()
