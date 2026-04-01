#Mini systeme de connexion

import logging #qui va me permettre d'enregistrer professionnellement les infos dans mon fichier .log
def connexion(mot):
    logging.basicConfig(
        filename = "logs\\rapport.log",
        level = logging.INFO,
        format = "%(asctime)s - %(levelname)s - %(message)s"
    )
    tentative = 0
    user = input("Veuillez entrer le mot de passe: ")
    while (tentative <3 and user != mot):
        tentative +=1
        print(f"Mot de passe incorrecte. Il vous reste {3-tentative} essais.")
        logging.warning(f"failed login")
        logging.info(f"tentative restante: {3-tentative}")
        if 3-tentative > 0: user = input("Veuillez saisir le mot de passe correcte s'il vous plaît: ")
    if tentative == 3 and user != mot:
        print("Trop de tentatives, accès refusé !")
        logging.warning(f"Trop de tentative, Accès refusé")
        return
    print("Accès autorisé !")
    logging.info(f"Accès autorisé")

mot = "ABC30"
connexion(mot)