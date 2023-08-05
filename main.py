import string
import random


def generateRandomLetters():
    randomletter = []
    i = 0
    while i != 3:
        letter = random.choice(string.ascii_letters)
        randomletter.append(letter)
        i = i + 1

    randomLetterStr = ""
    for element in randomletter:
        randomLetterStr += element

    return randomLetterStr


def code():
    codeWord = input("Write the word for coding")
    codeWord = codeWord.lower()
    if len(codeWord) >= 3:
        codeWord = codeWord[1:] + codeWord[0]
        codeWord = generateRandomLetters() + codeWord + generateRandomLetters()
        print(codeWord)
    else:
        codeWord = codeWord[::-1]
        print(codeWord)


def decode():
    decodeWord = input("Write the word to decode")
    if len(decodeWord) >= 3:
        decodeWord = decodeWord[3:-3]
        decodeWord = decodeWord[-1] + decodeWord[0:-1]
        print(f"The decode word is {decodeWord}")
    else:
        decodeWord = decodeWord[::-1]
        print(f"The decode word is {decodeWord}")


codeOrDecode = input("Do you want to code or decode?")
codeOrDecode = codeOrDecode.lower()


if codeOrDecode == "code":
    code()
elif codeOrDecode == "decode":
    decode()
else:
    print("Not a valid input")

# By Aditya Raj