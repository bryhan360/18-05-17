#!/usr/bin/python
# coding: utf8

palo = [ "P" , "C" , "D" , "T" ]

numero = [ "1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "10" , "11" , "12" , "13" ]

cont = 52

from random import randint

for palo in range (1,5,1):
	for numeros in range (1,14,1):
		
		palo = randint (1,4)
		numero = randint (1,13)
		
		if ( numero == 11 ):
			numero = "J"
		
		if ( numero == 12 ):
			numero = "Q"
		
		if ( numero == 13 ):
			numero = "K"
		
		if ( palo == 1 ):
			palo = "D"
		
		if ( palo == 2 ):
			palo = "C"			
		
		if ( palo == 3 ):
			palo = "T"			
		
		if ( palo == 4 ):
			palo = "P"
		
		print numero , palo
		
cont = cont - 1
