# Polyalphabetic Cipher (Vigenere Cipher)

text = input("Enter text: ").upper()
key = input("Enter key: ").upper()

result = ""
key_index = 0

choice = input("Enter E for Encrypt or D for Decrypt: ").upper()

for i in range(len(text)):
    if text[i].isalpha():
        t = ord(text[i]) - 65
        k = ord(key[key_index % len(key)]) - 65

        if choice == "E":
            value = (t + k) % 26
        else:   # Decryption
            value = (t - k) % 26

        result += chr(value + 65)
        key_index += 1
    else:
        result += text[i]

print("Result:", result)
