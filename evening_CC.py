alphabet = "abcdefghijklmnopqrstuvwxyz"


def isPangram(sentence):
    lowered = sentence.lower()
    for abc in alphabet:
        if abc not in lowered:
            return False
        else:
            return True


print(isPangram("asdfukhiuleflodsifjpdocvikzx[lcpwd[xscdwr235u6702-132="))
