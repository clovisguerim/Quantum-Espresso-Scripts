#!/bin/python3
"""
Este script verifica listas de funcoes de ondas dos orbitais p e s para determinados atomos (que tambem devem ser listados) e executa o modulo plotband.x do Quantum Espresso para plot da estrutura de bandas projetadas
"""

import os

filename = "ag977.bands_final"
fermi = "3.85"
atom_list = [52,31,38,48,42,41]
s_list1 = [[460],[271],[334],[370],[388],[361]]
p_list1 = [[461,462,463],[272, 273, 274], [335,336,337],[371,372,373],[389,390,391],[362,363,364]]
table = []
for j in range(len(atom_list)):
	atom_number=atom_list[j]
	s_list=s_list1[j]
	s_orbital=['s']
	p_list=p_list1[j]
	p_orbital =['px','py','pz']
	
	remove = 'rm banda.ps plot.out'
	plot = 'plotband.x < plot.in > plot.out'
	os.system(f'mkdir {atom_number}_s' )		
	for i in range(len(s_list)):
		f = open("plot.in", "w")
		f.write(filename) # nome do arquivo bands
		f.write("\n")
		f.write(f" {s_list[i]}")# lista de orbitais
		f.write("\n")
		f.write(" -4 9")# lintervalo de energia
		f.write("\n")
		f.write(f"atom_{atom_number}"f"_{s_orbital[i]}.gnu")# output de bands
		f.write("\n")
		f.write("banda.ps")
		f.write("\n")
		f.write(f" {fermi}")
		f.write("\n")
		f.write("\n")
		f.write(f"2.0 {fermi}")
		f.close()
		os.system(plot)
		
		os.system(remove)
		file = 'atom'+'_'+str(atom_number)+'_'+f'{s_orbital[i]}'+'.gnu'
		
			
		
		os.system(f'mv {file} {atom_number}_s' )
		
		
	os.system(f'mkdir {atom_number}_p' )
	for i in range(len(p_list)):
		f = open("plot.in", "w")
		f.write(filename) # nome do arquivo bands
		f.write("\n")
		f.write(f" {p_list[i]}")# lista de orbitais
		f.write("\n")
		f.write(" -4 9")# lintervalo de energia
		f.write("\n")
		f.write(f"atom_{atom_number}"f"_{p_orbital[i]}.gnu")# output de bands
		f.write("\n")
		f.write("banda.ps")
		f.write("\n")
		f.write(f" {fermi}")
		f.write("\n")
		f.write("\n")
		f.write("2.0 {fermi}")
		f.close()
		os.system(plot)
		os.system(remove)
		file = 'atom'+'_'+str(atom_number)+'_'+f'{p_orbital[i]}'+'.gnu'

			
		os.system(f'mv {file} {atom_number}_p' )


