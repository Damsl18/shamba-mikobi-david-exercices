#Script de recherche dans les logs
from collections import Counter
chemin ="logs\\fichier.log"
def RechercheLogs(chemin):
    i = 0 #pour nombre de lignes contenant "failed login"
    ip = []
    most = 0
    ipMost = ""
    with open(chemin, "r") as file:
        for line in file:
            if "failed login" in line:
                i += 1
            partie = line.strip().split(" - ")
            ip.append(partie[3])
    compteur = Counter(ip)
    for cle in ip:
        if compteur [cle] > most:
            most = compteur[cle]
            ipMost = cle
    print(f"RESUME FINAL\n"
          f"Il y a {i} ligne(s) contenant 'failed login'\n"
          f"Addresses IP: {ip}\n"
          f"IP la plus fréquente: {ipMost}  avec: {most} apparitions")

RechercheLogs(chemin)