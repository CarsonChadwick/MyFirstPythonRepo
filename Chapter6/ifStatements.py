# Prompt for song name
sSongName = input("Enter the song title: ")
#propt for the band
sBand = input("Enter the band name: ")
# Prompt for song ratingbetween 0 and 10
iRating = int(input("Enter the song rating between 0 and 10 (i.e. 10 is high): "))
# Determine if they liked the song
if (iRating >= 7) :
    if (sBand.upper() == "QUEEN") or (sBand.upper() == "ACDC") :
        print("They are awesome")
    else : 
        print("you must really like that song!")
        print("Let's go listen to it now")
elif (iRating >= 5) : 
    print("You sort of like that song")
elif (iRating >= 2) : 
    print("You must not like that song very much")    
else : 
    print("You hate that song")

print("Goodbye")


