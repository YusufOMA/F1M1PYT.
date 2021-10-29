  
import random

people = ["Waldo","Jackson","Ray","Eric","Vaughn","Jesse","Herbert","Robert", "Rodrigo","Elija","Sasha","Nathaniel","Ellie","Allison","Jeremiah", "Paula", "Alisha","Tory","Troy", "Faye"]

random.shuffle(people)

for x in people:

    print(x)

    if x == "Waldo":

        print("ik heb Waldo gevonden hij zit op nummer:"+str(people.index("Waldo"))+"")

        print(people)

        break