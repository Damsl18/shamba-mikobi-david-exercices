#ANALYSE DE MOTS
from collections import Counter
print("Veuillez insérer une phrase, n'importe")
phrase = input().lower().split()
def compter_mot(phrase):
    print(f'Le nombre de mot total inscript dans votre phrase est de : {len(phrase)}')

def plusLong(phrase):
    for i in range(len(phrase)):
        compteur = 0
        if (len(phrase[i]) > compteur):
            compteur = len(phrase[i])
            long = phrase[i]
    print(f'Le mot le plus long est: {long}')

def occurence(phrase):
    for mot, nombre in Counter(phrase).items():
        print(f'"{mot}" apparaît: {nombre} fois')

compter_mot(phrase)
plusLong(phrase)
occurence(phrase)