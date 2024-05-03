# Quiz sur (template)
from time import *

score = 0


# Vérification de la réponse
def answer():
    while True:
        try:
            u = int(input("Votre réponse : "))
            if 0 < u <= 4:
                return u
            else:
                print("Le chiffre doit être compris entre 1 et 4 !")
                continue
        except:
            print("Veuillez entrer un nombre")
            continue


def check(a: int):
    global score

    u = answer()

    if a == u:
        print("Bonne réponse !")
        score += 1
    else:
        print("Mauvaise réponse !")
    print("Score : " + str(score))
    sleep(2)
    print()


# Poser la question
def question(q: list):
    for i in q:
        print(i)


print("Bienvenue dans ce quiz sur (template) !")
print("Pour répondre, tapez simplement le bon chiffre.")
sleep(3)
print()

a = ["A) ",
     " 1) ", 
     " 2) ",
     " 3) ",
     " 4) "]
question(a)
check(2)

print("Vous avez fini le quiz avec ", score, " points")
