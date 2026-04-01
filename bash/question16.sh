#!/bin/bash

touch rapport_systeme.txt
hostname > rapport_systeme.txt
uname >> rapport_systeme.txt
hostname -I >> rapport_systeme.txt
df -h >> rapport_systeme.txt
free -h >> rapport_systeme.txt
who >> rapport_systeme.txt
