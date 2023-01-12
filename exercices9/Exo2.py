def chiffre_xor(s, key):
    return bytes([s[i] ^ key[i % len(key)] for i in range(len(s))])