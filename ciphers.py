def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - start + shift) % 26 + start) if mode == "encrypt" else chr((ord(char) - start - shift) % 26 + start)
            result += shifted_char
        else:
            result += char
    return result

def reverse_cipher(text):
    return text[::-1]

def atbash_cipher(text):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr(ord('a') + ord('z') - ord(char))
            else:
                result += chr(ord('A') + ord('Z') - ord(char))
        else:
            result += char
    return result