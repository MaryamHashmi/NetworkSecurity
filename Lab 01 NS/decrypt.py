#decrypt

def decrypt(message):
    decrypted = ''
    key = -2
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

        decrypted += chr(code)
    return decrypted


one = "JgnnqYqtnf"
print decrypt(one)
