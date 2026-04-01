#Validation d'un mot de passe
print('En insérant un mot de passe, respectez les instructions suivantes:\n'
      '1. Au moins 10 caractères\n'
      '2. Au moins une lettre majuscule\n'
      '3. Au moins une lettre minuscule\n'
      '4. Au moins un caractère spécial')
debut = "Votre code doit avoir"
regles = ["Au moins 10 caractères", "Au moins une lettre majuscule", "Au moins une lettre minuscule", "Au moins un chiffre", "Au moins un caractère spécial"]
def caractere(mot):
    if (len(mot) >= 10):
        return True
    print(f'{debut} {regles[0]}')
def majuscule(mot):
    for letter in mot:
        if(not (letter.isdigit()) and (letter.upper() == letter)): return True
    print(f'{debut} {regles[1]}')
def minuscule(mot):
    for letter in mot:
        if(not (letter.isdigit()) and (letter.lower() == letter)):
            return True
    print(f'{debut} {regles[2]}')
def chiffre(mot):
    for letter in mot:
        if(letter.isdigit()):
            return True
    print(f'{debut} {regles[3]}')
def special(mot):
    for letter in mot:
        for i in letter:
            if(not(i.isdigit) or not(i.isalpha()) and not(i.isdigit())):
                return True
    print(f'{debut} {regles[4]}')
def validation(mot):
    caractere(mot)
    majuscule(mot)
    minuscule(mot)
    chiffre(mot)
    special(mot)
mot = input("\nVeuillez inscrire votre mot de passe s'il vous plaît: ")
validation(mot)
