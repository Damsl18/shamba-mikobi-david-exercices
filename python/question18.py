#Gestion d'un fichier csv
import csv
path = "logs\\text.csv"
def afficher_etudiant(path):
    i = 0
    with open(path, "r", encoding='UTF-8') as fichier:
        file = csv.reader(fichier)
        for line in file:
            i += 1
            print(f'Etudiant {i}: {line[0]}')
def moyenne_generale(path):
    total = 0
    somme = 0
    with open(path, "r") as fichier:
        file = csv.reader(fichier)
        for line in file:
            total += 1
            somme += int(line[1])
        moyenne = somme/total
        print(f'La moyenne générale est de: {moyenne}')

def meilleur_cote(path):
    score = 0
    best = [""]
    with open(path, "r") as fichier:
        file = csv.reader(fichier)
        for line in file:
            if (int(line[1]) > score):
                best[0] = line[0]
                score = int(line[1])
            elif (int(line[1]) >= score):
                best.append(line[0])
    print(f"L'(s) étudiant(s) avec la plus grande cote: {score} est (sont): {best}")

def cote_inferieure(path):
    with open(path, "r", encoding='UTF-8') as fichier:
        file = csv.reader(fichier)
        for line in file:
            if (int(line[1]) < 10):
                print(f"L'étudiant(e): {line[0]} a une note inférieure à 10: {line[1]}")
afficher_etudiant(path)
moyenne_generale(path)
meilleur_cote(path)
cote_inferieure(path)