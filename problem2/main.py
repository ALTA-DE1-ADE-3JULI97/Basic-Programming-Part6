def caesar(offset, input_str):
    shifted_str = ""
    for char in input_str:
        if char.isalpha():
            ascii_val = ord(char.lower()) - ord('a')  # Convert to 0-based index
            shifted_ascii_val = (ascii_val + offset) % 26  # Modulo operator for wrapping
            shifted_char = chr(shifted_ascii_val + ord('a'))  # Convert back to ASCII character
            if char.isupper():
                shifted_char = shifted_char.upper()  # Preserve original case
            shifted_str += shifted_char
        else:
            shifted_str += char  # Preserve non-alphabetic characters
    return shifted_str

if __name__ == '__main__':
    print(caesar(3, "abc")) # def
    print(caesar(2, "alta")) # cnvc
    print(caesar(10, "alterraacademy")) # kvdobbkkmknowi
    print(caesar(1, "abcdefghijklmnopqrstuvwxyz")) # bcdefghijklmnopqrstuvwxyza
    print(caesar(1000, "abcdefghijklmnopqrstuvwxyz")) # mnopqrstuvwxyzabcdefghijkl