#Surveillance de fichier, on est dans le cas où il n ' y a que des fichier dans le dossier
import os
def analyse ( dossier ):
    if not os.path.exists(dossier):
        print(f"Le dossier: {dossier} n'existe pas")
    taille = 0.0
    bestTaille = 0.0
    plusGros = ""
    total = 0.0

    for file in os.listdir(dossier):
        path = os.path.join(dossier, file)
        if os.path.isfile(path):
            taille = os.path.getsize(path)
            total += taille
            print(f"{file} taille: {taille/2**20:.2f}M")
            if taille > bestTaille:
                bestTaille = taille
                plusGros = file
    print(f"Le plus gros fichier est: {plusGros} de taille: {bestTaille/2**20:.2f}M")
    print(f"Voici la taille totale du dossier: {total/2**30:.2f} Giga")

dossier ="D:\\mes images windows"
analyse(dossier)
