#Vokabeltrainer
import random
vokabeln = [["Tisch", "table"], ["Auto", "car"], ["Haus", "house"]]
print(vokabeln)
random.shuffle(vokabeln)
print(vokabeln)
print("Übersetze auf Englisch")
for vok in vokabeln:
    eingabe = input(vok[0] + " : ")
    if eingabe == vok[1]:
        print("Richtig!")
    else:
        print("Leider falsch!")
