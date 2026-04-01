#!/bin/bash
echo "sccript qui va parcourir les nombres de 1 à 50"
for i in {1..50} ; do
	if [ $((i%3)) -eq 0 ]; then
		echo "Fizz"
	elif [ $((i%5)) -eq 0 ]; then
		echo "Buzz"
	fi
	if [[ $((i%3)) -eq 0 && $((i%5)) -eq 0 ]]; then
	       echo "FizzBuzz"
	fi	       
done
