#J'ai fait ce script pour me permettre de remplir d'informations factisses d'un fichier
#.log afin de concrétiser la question 23

import random
import logging
logging.basicConfig(
    filename = "logs\\fichier.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)
choix = ["failed login", "login successfull", "error login", "RAS", "Beaucoup autres informations"]
state = [0, 1, 2, 3, 4]
ip = ["192.168.15.1", "192.168.409.1", "192.168.4.4", "172.26.101.0", "10.10.18.1", "192.168.70.1", "192.168.240.1", "192.168.455.0", "172.16.122.0", "10.5.32.1", "192.168.1.1", "192.168.2.1", "192.168.230.0", "172.16.13.0", "10.0.7.1"]
taille = len(ip)
tableau1 =[]
tableau2 = []
for i in range(200):
    tableau1.append(i)
for j in range (taille):
    tableau2.append(j)

for i in range (200):
    test2 = random.choice(tableau2)
    test3 =  random.choice(state)
    logging.info(f"{choix[test3]} - {ip[test2]}")
    test2 = random.choice(tableau2)
    test3 =  random.choice(state)
    logging.warning(f"{choix[test3]} - {ip[test2]}")
    test2 = random.choice(tableau2)
    test3 =  random.choice(state)
    logging.error(f"{choix[test3]} - {ip[test2]}")
print("FINITO")
