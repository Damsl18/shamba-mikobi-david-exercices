#Gestion d'un fichier csv
import csv
path = "logs\\text.csv"
def gestion_fichier(path):
    i = 0
    total = 0
    somme = 0
    score = 0
    best = [""]
    with open(path, "r", encoding='UTF-8') as fichier:
        file = csv.reader(fichier)
        for line in file:
            i += 1
            print(f'Etudiant {i}: {line[0]}')
            total += 1
            somme += int(line[1])
            if (int(line[1]) > score):
                best[0] = line[0]
                score = int(line[1])
            elif (int(line[1]) >= score):
                best.append(line[0])
            if (int(line[1]) < 10):
                print(f"L'étudiant(e): {line[0]} a une note inférieure à 10: {line[1]}")
        moyenne = somme/total
        print(f'La moyenne générale est de: {moyenne}')
        print(f"L'(s) étudiant(s) avec la plus grande cote: {score} est (sont): {best}")
gestion_fichier(path)
