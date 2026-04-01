#!/bin/bash*-
echo "veuillez insérer le nom du fichier s'il vous plaît"
read nom
if [ -f "$nom" ]; then
	echo "le fichier existe"
	echo "taille: "
	du -h $nom
	echo " droits: "
        ls -ld $nom
else
       echo "le fichier n'existe pas"
fi
	
