print("DIE!")
def count_vowel(s):
    numA = s.count("a")
    numE = s.count("e")
    numI = s.count("i")
    numO = s.count("o")
    numU = s.count("u")
    sumVowels = numA + numE + numI + numO + numU
    if numA == 0 and numE == 0 and numI == 0 and numO == 0 and numU == 0:
        numY = s.count("y")
    sumVowels = numY
    return sumVowels
print(count_vowel(raw_input("enter yourself")))
