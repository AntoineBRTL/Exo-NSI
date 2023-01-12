def dechiffrement(texte_a_dechiffrer, n):
    a = "abcdefghijklmnopqrstuvwxyz"
    texte_chiffre = ""
    for e in texte_a_dechiffrer:
        if(e == " "):
            texte_chiffre += " "
            continue
        if(e == "!"):
            texte_chiffre += "!"
            continue

        texte_chiffre += a[(a.rfind(e) - n) % 26]
        #texte_chiffre += chr((((ord(e) - n) - 97) % 26) + 97)

    return texte_chiffre

print(dechiffrement("qf hwduytlwfumnj jxy zynqnxjj qjx sfanlfyjzwx bjg !", 5))