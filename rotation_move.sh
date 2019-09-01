#!/bin/bash
for i in L L\' L2 R R\' R2 F F\' F2  D D\' D2 U U\' U2 B  B\' B2
do
	echo "move $i"
	python3 ./visualisation/ascii_template.py "$i"
done
