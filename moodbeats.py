import json
import random

with open("songs.json","r") as file:
    songs = json.load(file)

mood = input("Enter your mood (happy, sad, energetic, relaxed): ").strip().lower()

if mood in songs:
    ice = random.choice(songs[mood])
    nt = input(f"Do you want to listen to '{ice}'? (yes/no): ").strip().lower()
    if nt == "yes":
        print(f"Great! Enjoy listening to '{ice}'!")
    elif nt == "no":
        print("No problem! Let's find another song.")
        ice = random.choice(songs[mood])
        print(f"How about '{ice}'? Do you want to listen to it? (yes/no): ")
        nt = input().strip().lower()
        if nt == "yes":
            print(f"Great! Enjoy listening to '{ice}'!")
        else:
            print("Okay, feel free to explore more songs later!")
else:
    print("Sorry, I don't have songs for that mood. Please try again with a different mood.")
    exit()

    