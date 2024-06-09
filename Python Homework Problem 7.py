def encipher_fence(plaintext,numRails):
    railList = []
    rail = ''
    for place in range(numRails):
        num = place
        while num + 1 <= len(plaintext):
            rail += plaintext[num]
            num += numRails
        railList.append(rail)
        rail = ''
    railList.reverse()
    return ''.join(railList)

def decipher_fence(ciphertext,numRails): # I need help here
    return None # not completed

def decode_text(ciphertext,wordfilename): # I also need help here
    return None # not completed

# test cases

# enciphering
print(encipher_fence("abcdefghi", 3))
# should print: cfibehadg
print(encipher_fence("This is a test.", 2))
# should print: hsi  etTi sats.
print(encipher_fence("This is a test.", 3))
# should print: iiae.h  ttTss s
print(encipher_fence("Happy birthday to you!", 4))
# should print: pidtopbh ya ty !Hyraou

# deciphering
print(decipher_fence("hsi  etTi sats.", 2))
# should print: This is a test.
print(decipher_fence("iiae.h  ttTss s", 3))
# should print: This is a test.
print(decipher_fence("pidtopbh ya ty !Hyraou", 4))
# should print: Happy birthday to you!

# decoding
print(decode_text(" cr  pvtl eibnxmo  yghu wou rezotqkofjsehad", 'wordlist.txt'))
# should print: the quick brown fox jumps over the lazy dog
print(decode_text("unt S.frynPs aPiosse  Aa'lgn lt noncIniha ", 'wordlist.txt'))
# should print... we'll let you find out!
[uploadedFile="wordlist.txt"][/uploadedFile]
