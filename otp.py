
import glob
import random
import time
from bitstring import BitArray, Bits, BitStream
import os
import sys


def keyboardinputcoinfliprng():

    timestr = time.strftime("%Y%m%d%H%M%S")

    def split4(txt):
        return " ".join("".join(txt[i : i + 4]) for i in range(0, len(txt), 4))

    userinput = input("type some words and press return: ")

    encodeduserinput = userinput.encode("utf-8")

    msgbits = BitArray(encodeduserinput)

    print("message bits: " + split4(msgbits.bin))

    bitlength = msgbits.len
    cointosses = input("enter at least " + str(bitlength) + " ones and zeroes: ")
    cointossbitarray = BitArray(bin=cointosses)
    cointossbitstream = BitStream(cointossbitarray)
    key = cointossbitstream.read(bitlength)

    cipher = BitArray(msgbits ^ key)

    cipherfilename = timestr + "msgpart1.txt"
    keyfilename = timestr + "msgpart2.txt"

    ciphertext = open(cipherfilename, "w")
    ciphertext.write(cipher.bin)
    print("message bits: " + split4(msgbits.bin))
    print("key bits:     " + split4(key.bin))
    print("cipher bits:  " + split4(cipher.bin))
    print("message bits: " + split4(msgbits.hex))
    print("key bits:     " + split4(key.hex))
    print("cipher bits:  " + split4(cipher.hex))    
    ciphertext.close()

    keytext = open(keyfilename, "w")
    keytext.write(key.bin)
    keytext.close()

def decrypt():
    for filename in glob.glob("*msgpart1.txt"):
        ciphercontent = open(filename, "r").read()
    ciphertext = BitArray(bin=ciphercontent)

    for filename in glob.glob("*msgpart2.txt"):
        keycontent = open(filename, "r").read()
    keytext = BitArray(bin=keycontent)
    input("Press enter to exit")

    decode = (ciphertext ^ keytext).bytes.decode()
    print(decode)

print(20 * "-")
print("1. Encrypt keyboard input to text files, RNG: coin flips entered on keyboard")
print("2. Decrypt. Make sure the message parts of only the current message")
print("are in the folder containing the otp program.")
print(20 * "-")

choice = input("Enter your choice: ")

choice = int(choice)

if choice == 1:
    print("Encrypting keyboard input...")
    keyboardinputcoinfliprng()
elif choice == 2:
    print("Decrypting...")
    decrypt()

else:  ## default ##
    print("Invalid number. Try again...")
