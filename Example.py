# Quiz informatique
from time import *

score = 0


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


def question(q: list):
    for i in q:
        print(i)


print("Bienvenue dans ce quiz sur l'informatique !")
print("Pour répondre, tapez simplement le bon chiffre.")
sleep(3)
print()

a = ["A) Quel est le nom du premier langage de programmation ?",
     " 1) Le Java", " 2) Le Fortran",
     " 3) Le JavaScript",
     " 4) Le Markdown"]
question(a)
check(2)

b = ["B) Combien de bits faut il pour coder une couleur ?",
     " 1) 4",
     " 2) 13",
     " 3) 24",
     " 4) Mmmmh"]
question(b)
check(3)

c = ["C) Quelle couleur donnera le code RGB suivant ? RGB(255, 255, 255)",
     " 1) Blanc"
     " 2) Gris"
     " 3) Cyan"
     " 4) Vert"]
question(c)
check(1)

d = ["D) Lequel de ces noms n'est pas une distro linux ?",
     " 1) Steam OS ",
     " 2) Linux mint",
     " 3) Obonto",
     " 4) pop_!os"]
question(d)
check(3)

e = ["E) Quel est le site le plus utilisé par les développeurs ?",
     " 1) GitHub",
     " 2) Stack Overflow",
     " 3) LFS"
     " 4) Youtube"]
question(e)
check(1)

f = ["F) Quel est le langage de programmation le plus utilisé ?",
     " 1) Java",
     " 2) Pascal",
     " 3) Python",
     " 4) C"]
question(f)
check(3)

g = ["G) Quel est l'output de ce calcul ? (5 * 2)**2 - 8",
     " 1) 102",
     " 2) 92",
     " 3) 64",
     " 4) Je sais pas"]
question(g)
check(2)

h = ["H) Quel est la plus ancienne version de windows parmi celles ci ?",
     " 1) Windows XP",
     " 2) Windows",
     " 3) Windows 95",
     " 4) Mac OS X"]
question(h)
check(2)

i = ["I) Quel est le nom du gestionnaire de paquet de Node.js ?"
     " 1) NPM",
     " 2) PiPy",
     " 3) Yarn",
     " 4) Node"]
question(i)
check(1)

j = ["J) Quel est le nom du premier réseau informatique ?",
     " 1) Internet",
     " 2) SFR",
     " 3) Arpanet",
     " 4) Le cerveau d'Elon Musk"]
question(j)
check(3)

k = ["K) Quel type de fichier ci dessous est l'intrus ?",
     " 1) .py",
     " 2) .mp3",
     " 3) .java",
     " 4) .h"]
question(k)
check(2)

l = ["L) Quel élément ci dessous ne fait pas parti d'un ordinateur ?",
     " 1) La carte mère",
     " 2) Le SSD",
     " 3) Le disjoncteur",
     " 4) La ventilation"]
question(l)
check(3)

m = ["M) Quel nom ci dessous n'est pas un langage de programmation ?",
     " 1) Le Brainfuck",
     " 2) Le LolCode",
     " 3) Le Shakespeare Programming Language",
     " 4) Le melon"]
question(m)
check(4)

m = ["M) Quel est le binaire de 'Melon' ?",
     " 1) 0100110101100101011011000110111101101110",
     " 2) 1211212112121212112121121222111122221111",
     " 3) Juste 'Melon' sois pas chiant",
     " 4) J'aime pas les règles : 4D 65 6C 6F 6E 0A"]
question(m)
check(1)

n = ["N) À quoi correspond l'erreur 404 ?",
     " 1) A une erreur serveur",
     " 2) Mon cerveau ne réponds plus",
     " 3) La page n'existe pas",
     " 4) Je préfère 666"]
question(n)
check(3)

print("Vous avez fini le quiz avec ", score, " points")
