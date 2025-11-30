print("Welcome to the Manga Reader Recommender!!")

genre = input("Choose a genre (action, romance, horror): ")
length = input("Choose a length (short, medium, long): ")
decade = input("Choose a decade (2000, 2010): ")

if genre == "action" and length == "long" and decade == "2010":
    print("You should read: Nanatzu No Taizai ")
elif genre == "romance" and length == "short" and decade == "2010":
    print("You should read: Your Name, and Horimiya")
elif genre == "horror" and length == "long" and decade == "2010":
    print("You should read: Toilet Bound Hanako Kun")
elif genre == "action" and length == "medium" and decade == "2010":
    print("You should read Jujutsu Kaisen")
elif genre == "action" and length == "medium" and decade == "2000":
    print("You should read Inuyasha ")
else:
    print("Sorry, no manga found for your choices, come back later!")
    
