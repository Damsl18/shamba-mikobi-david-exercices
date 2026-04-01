#!/bin/bash

echo "on va créer des utilisateurs à partir d'un fichier text"
echo "entrez le nom ou chemin du fichier"
read fichier

if [ ! -f "$fichier" ]; then
	echo "Desolé, votre fichier [$fichier] n'existe pas"
	exit 1
fi

while read f; do
	sudo useradd -m $f
	echo "$f:test123" | sudo chpasswd
	sudo chage -d 0 $f
	echo "Utilisateur: $f créé avec succès"
done < $fichier
