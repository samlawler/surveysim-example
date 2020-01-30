#! /bin/sh

for i in 0 1 2 3 4 5 6 7 8 9; do
	for j in 0 1 2 3 4 5 6 7 8 9; do
		python Driver.py
		wc -l drawn.dat >> pops.dat
	done
done

rm drawn.dat
