import binascii
import fileinput

def bin2hex(str1):
	n = int(str1, 2)
	cadena = str(hex(n))[2:]
	while len(cadena) < 8: # siempre son de 8 caracteres en hexa
		cadena = '0' + cadena
	return cadena

for line in fileinput.input():
	sinEsp = line.replace(" ", "") #fuera espacios
	print(str(bin2hex(sinEsp)))
