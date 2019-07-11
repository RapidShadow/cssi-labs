
print("Hello World")
characterNum = 1
myString = raw_input("Give me a string loop though: ")
for character in myString:
    print("This is letter number %s" % (characterNum))
    characterNum = characterNum + 1
    print(character)
