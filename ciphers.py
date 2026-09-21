def caesar_cipher(text):
    try:
        # Find the opening and closing parentheses
        start_index = text.find("(")
        end_index = text.find(")")

        if start_index == -1 or end_index == -1 or end_index <= start_index:
            return None, None  # Invalid format

        # Extract the number string and shift value
        number_str = text[start_index + 1:end_index]
        shift_value = int(number_str)

        # Extract the text to be shifted
        text_to_shift = text[end_index + 1:]

        if shift_value == 0:
            return shift_value, text_to_shift  # No shift needed

        shifted_text = ""
        for char in text_to_shift:
            if 'a' <= char <= 'z':
                shifted_char = chr(((ord(char) - ord('a') + shift_value) % 26) + ord('a'))
            elif 'A' <= char <= 'Z':
                shifted_char = chr(((ord(char) - ord('A') + shift_value) % 26) + ord('A'))
            else:
                shifted_char = char  # Non-alphabetic characters remain unchanged
            shifted_text += shifted_char

        return shift_value, shifted_text

    except ValueError:
        return None, None  # Invalid number format
    except Exception as e:
        return None, None

def reverse_cipher(text):
    """
    Reverses the input string.

    Args:
        text: The input string.

    Returns:
        The reversed string.
    """
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