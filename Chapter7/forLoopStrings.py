# prompt the user for some letters
# for each letter have the user specify a word starting with that letter
# confirm they did it correctly

sList = input("Type the alphabet characters to practice: ")

for sChar in sList :
    sInput = input("Enter a word starting with the letter " + sChar + ": ")
    if (sChar.upper() == sInput[0].upper()) :
        print("Good job")
    else :
        print("You need to practice.")
