import math

# -*- coding: utf-8 -*-

class Alfabeto:

	def __init__(self):
		self.numberToCharacterSpanish = {"A": 0, "B": 1, "C": 2, "D": 3, "E" : 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, 
											"K": 10, "L": 11, "M": 12, "N": 13, "Ñ": 14, "O": 15, "P": 16, "Q": 17, "R": 18, 
											"S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}

		self.characterToNumberSpanish = {0: "A", 1: "B", 2: "C", 3: "D", 4:"E", 5:"F", 6:"G", 7:"H", 8:"I", 9:"J", 10:"K", 
											11:"L", 12:"M", 13:"N", 14:"Ñ", 15:"O", 16:"P", 17:"Q", 18:"R", 19:"S", 20:"T", 
											21:"U", 22:"V", 23:"W", 24:"X", 25:"Y", 26:"Z"}

		self.numberToCharacterEnglish = {"A": 0, "B": 1, "C": 2, "D": 3, "E" : 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, 
											"K": 10, "L": 11, "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, 
											"T": 19, "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25}

		self.characterToNumberEnglish = {0: "A", 1: "B", 2: "C", 3: "D", 4:"E", 5:"F", 6:"G", 7:"H", 8:"I", 9:"J", 10:"K", 
											11:"L", 12:"M", 13:"N", 14:"O", 15:"P", 16:"Q", 17:"R", 18:"S", 19:"T", 20:"U", 
											21:"V", 22:"W", 23:"X", 24:"Y", 25:"Z"}

		self.numberToCharacterBase64 = {0: "A", 1: "B", 2: "C", 3: "D", 4:"E", 5:"F", 6:"G", 7:"H", 8:"I", 9:"J", 10:"K", 
											11:"L", 12:"M", 13:"N", 14:"O", 15:"P", 16:"Q", 17:"R", 18:"S", 19:"T", 20:"U", 
											21:"V", 22:"W", 23:"X", 24:"Y", 25:"Z", 26: "a", 27: "b", 28: "c", 29: "d", 30:"e",
											31:"f", 32:"g", 33:"h", 34:"i", 35:"j", 36:"k", 37:"l", 38:"m", 39:"n", 40:"o", 41:"p",
											42:"q", 43:"r", 44:"s", 45:"t", 46:"u", 47:"v", 48:"w", 49:"x", 50:"y", 51:"z", 52:"0",
											53:"1", 54:"2", 55:"3", 56:"4", 57:"5", 58:"6", 59:"7", 60:"8", 61:"9", 62:"+", 63:"/"}

		self.characterToNumberBase64 = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9, "K":10, 
											"L":11, "M":12, "N":13, "O":14, "P":15, "Q":16, "R":17, "S":18, "T":19, "U":20, 
											"V":21, "W":22, "X":23, "Y":24, "Z":25, "a":26, "b":27, "c":28, "d":29, "e":30,
											"f":31, "g":32, "h":33, "i":34, "j":35, "k":36, "l":37, "m":38, "n":39, "o":40, "p":41,
											"q":42, "r":43, "s":44, "t":45, "u":46, "v":47, "w":48, "x":49, "y":50, "z":51, "0":52,
											"1":53, "2":54, "3":55, "4":56, "5":57, "6":58, "7":59, "8":60, "9":61, "+":62, "/":63}


	def codTextoToBase64(self, texto):
		cont = 0
		textoBinary = ""
		tamTexto = len(texto)
		
		while(cont < tamTexto):
			ascii_word = ord(texto[(cont):(cont+1)])
			binary_word = bin(ascii_word)[2:].zfill(8)
			
			textoBinary += binary_word
			cont += 1

		tamTextoBinary = len(textoBinary)
		ciclos = int(tamTextoBinary/6)
		contCiclo = 0
		textoBase64 = ""
		final = ""
		
		while(contCiclo <= ciclos):
			posInicial = contCiclo * 6
			posFinal = (contCiclo+1) * 6
			numBinary = textoBinary[posInicial:posFinal]
			#print(str(numBinary))
			if(len(numBinary) < 6):
				numBinary = numBinary.ljust(6, '0')
				#final += "="
			
			intBinary = int(numBinary,2)
			#if(intBinary > 1):
			textoBase64 += self.numberToCharacterBase64[intBinary]
			contCiclo += 1
		#textoBase64 += final

		return textoBase64

	def desCodBase64ToTexto(self, texto):

		cont = 0
		textoBinary = ""
		final = ""
		caracterQuitar = 0
		dosUltimos = texto[(len(texto)-2):(len(texto))]
		ultimos = texto[(len(texto)-1):(len(texto))]

		if(dosUltimos == "=="):
			caracterQuitar = 4
			texto = texto[0:(len(texto)-2)]
		elif(ultimos == "="):
			caracterQuitar = 2
			texto = texto[0:(len(texto)-1)]

		tamTexto = len(texto)
		while(cont < tamTexto):
			letra = texto[(cont):(cont+1)]
			intBinary = self.characterToNumberBase64[texto[(cont):(cont+1)]]
			numBinary = bin(intBinary)[2:].zfill(6)
			textoBinary += numBinary		
			cont += 1
		if(caracterQuitar > 0):
			textoBinary = textoBinary[0:(len(textoBinary)-caracterQuitar)]

		tamTextoBinary = len(textoBinary)
		ciclos = math.ceil(tamTextoBinary/8)

		#print("ciclos: "+str(ciclos))
		contCiclo = 0
		base64Texto = ""
		while(contCiclo < ciclos):

			posInicial = contCiclo * 8
			posFinal = (contCiclo+1) * 8
			numBinary = textoBinary[posInicial:posFinal]
			#intBinary = str(intBinary).ljust(8,"0")
			if(len(numBinary) < 8):
				print("Aqui: "+numBinary)
			intBinary = int(numBinary,2)

			''' RESOLVER
			tam = len(textoBinary[posInicial:(len(textoBinary))])
			if(tam < 8):
				textoBinary += "0"*(8-tam)
			'''

			if(intBinary > 0):
				base64Texto += chr(intBinary)
			contCiclo += 1

		return base64Texto
		
