# Encrypt
import sys

def encrypt(message):
    encrypted = ''
    key = 2
    for chara in message:
        if chara.isalpha():
            code = ord(chara)
            code = code + key

            if chara.isupper():
                if code > ord('Z'):
                    code -= 26
                elif code < ord('A'):
                    code += 26

            elif chara.islower():
                if code > ord('z'):
                    code -= 26
                elif code < ord('a'):
                    code += 26

            encrypted += chr(code)
    return encrypted




