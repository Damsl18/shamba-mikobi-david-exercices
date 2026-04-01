#!/bin/bash
echo "Veuillez entrer le nom du fichier"
read fichier
echo "voici le nombre de ligne du fichier: "
wc -l $fichier
echo "voici le nombre de linge contenant le mot ERROR: "
grep "ERROR" $fichier | wc -l
echo "voici le nombre de ligne contenant le mot WARNING: "
grep "WARNING" $fichier | wc -l
echo "voici les trois dernères lignes du fichier: "
tail -3 $fichier
