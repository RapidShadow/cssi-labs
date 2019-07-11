word = raw_input("Gimme word I make plural. ")
amount = int(raw_input("What is the amount? "))
if amount == 0:
    print("You have %d of %s. So %s stays the same" % (amount , word , word , word))
elif amount > 1:
    print("You have %d of %s. So %s becomes %ss" % (amount , word , word , word))
elif amount == 1:
    print("You have %d of %s. So %s stays the same" % (amount , word , word , word))
