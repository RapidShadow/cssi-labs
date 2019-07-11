print("Welcome >:C")
# Triangle Test
# triangle_side1 = int(raw_input("Enter your 1st triangle side length: "))
# triangle_side2 = int(raw_input("Enter your 2nd triangle side length: "))
# triangle_side3 = int(raw_input("Enter your 3rd triangle side length: "))
# def is_triangle(s1, s2, s3):
#     sum1 = s1 + s2
#     sum2 = s1 + s3
#     sum3 = s2 + s3
#     if sum1 > s3 and sum2 > s2 and sum3 > s1:
#         print("That is a real triangle")
#         return True
#     else:
#         print("That isn't a real triangle")
#         return False
# is_triangle(triangle_side1, triangle_side2, triangle_side3)
import random
numberOfSides = int(raw_input("Gimme a the number of sides on the die: "))
def dice(sides):
    return random.randint(1,sides)

def dicerollconfirm(data):
    roll = dice(data)
    print("Your roll is %d" % (roll))

dicerollconfirm(numberOfSides)

#reverse_string
# word = raw_input("give me a word: ")
# def reverse_string(x):
#     return x[::-1]
# print("Your word backwards is %s" % (reverse_string(word)))
