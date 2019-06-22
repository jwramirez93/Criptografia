from Alfabeto import Alfabeto

# Clase representación metodo Criptografico Vigenere con codificacion Base24
class Vigenere:
	
	def __init__(self):
		self.textoClaro = ''
		self.textoCifrado = ''
		self.clave = ''
		self.language = 0

	def cifrar(self):
		cont = 0
		contAux = 0
		textoCif = ""
		auxClave = self.clave
		auxClave = auxClave.replace("\n", "")
		tamClave = len(auxClave)
		alfabeto = Alfabeto()
		
		#texto = self.textoClaro
		if(self.language == "ascii"):
			texto = alfabeto.codTextoToBase64(self.textoClaro)
		else:
			texto = self.textoClaro
		#print("Base64: "+texto)
		tamTexto = len(texto)
		clave = self.clave
		# Se inicia un ciclo para recorrer todas las letras del texto a cifrar
		while(cont < tamTexto):
			# Se valida que el tamaño del alfabeto sea 27 para trabajar con el arreglo indicado
			letraTexto = texto[(cont):(cont+1)]
			if(self.language == 27):
				# Se recorre todo el tamaño de la clave, al finalizar, se toma la primera letra del texto en claro
				if(cont < tamClave):
					numberLetraClave = alfabeto.numberToCharacterSpanish[clave[(cont):(cont+1)]]
				else:
					numberLetraClave = alfabeto.numberToCharacterSpanish[texto[(contAux):(contAux+1)]]
					contAux += 1
				# Se extrae la posición de la letra y se realiza la operación de cifrado
				numberLetraMsj = alfabeto.numberToCharacterSpanish[texto[(cont):(cont+1)]]
				textoCif += alfabeto.characterToNumberSpanish[(numberLetraClave + numberLetraMsj) % 27]
			# Se valida que el tamaño del alfabeto sea 26 para trabajar con el arreglo indicado
			elif(self.language == 26):
				# Se recorre todo el tamaño de la clave, al finalizar, se toma la primera letra del texto en claro
				if(cont < tamClave):
					#if()
					letraNumberClave = alfabeto.numberToCharacterEnglish[clave[(cont):(cont+1)]]
				else:
					letraNumberClave = alfabeto.numberToCharacterEnglish[textoClaro[(contAux):(contAux+1)]]
					contAux += 1
				# Se extrae la posición de la letra y se realiza la operación de cifrado
				letraNumberMsj = alfabeto.numberToCharacterEnglish[textoClaro[(cont):(cont+1)]]
				textoCif += alfabeto.characterToNumberEnglish[(letraNumberMsj + letraNumberClave) % 26]
			elif(self.language == "ascii"):
				# Se recorre todo el tamaño de la clave, al finalizar, se toma la primera letra del texto en claro
				if(cont < tamClave):
					#print("-"+clave[(cont):(cont+1)]+"-")
					numberLetraClave = alfabeto.characterToNumberBase64[clave[(cont):(cont+1)]]
					letraClave = clave[(cont):(cont+1)]
				else:
					
					numberLetraClave = alfabeto.characterToNumberBase64[texto[(contAux):(contAux+1)]]
					letraClave = texto[(contAux):(contAux+1)]
					contAux += 1
				# Se extrae la posición de la letra y se realiza la operación de cifrado
				numberLetraMsj = alfabeto.characterToNumberBase64[texto[(cont):(cont+1)]]
				textoCif += alfabeto.numberToCharacterBase64[(numberLetraClave + numberLetraMsj) % 64]
				#print("LetraClaro: "+(texto[(cont):(cont+1)])+" ("+str(numberLetraMsj)+") - LetraClave: "+(letraClave)+" ("+str(numberLetraClave)+") - NumCif: "+(str((numberLetraClave + numberLetraMsj) % 64)))
			
			cont += 1

		return textoCif


	def descifrar(self):
		cont = 0
		contAux = 0
		textoDescif = ""
		auxClave = self.clave
		auxClave = auxClave.replace("\n", "")
		tamClave = len(auxClave)
		alfabeto = Alfabeto()

		texto = self.textoCifrado
		tamTexto = len(texto)
		clave = self.clave
		
		# Se inicia un ciclo para recorrer todas las letras del texto a descifrar
		while(cont < tamTexto):
			# Se valida que el tamaño del alfabeto sea 27 para trabajar con el arreglo indicado
			if(self.language == 27):
				# Se recorre todo el tamaño de la clave, al finalizar, se toma la primera letra del texto en descifrado
				if(cont < tamClave):
					numberLetraClave = alfabeto.numberToCharacterSpanish[clave[(cont):(cont+1)]]
				else:
					numberLetraClave = alfabeto.numberToCharacterSpanish[textoDescif[(contAux):(contAux+1)]]
					contAux += 1
				# Se extrae la posición de la letra y se realiza la operación de descifrado
				numberLetraMsj = alfabeto.numberToCharacterSpanish[texto[(cont):(cont+1)]]
				textoDescif += alfabeto.characterToNumberSpanish[(numberLetraMsj - numberLetraClave) % 27]
			# Se valida que el tamaño del alfabeto sea 26 para trabajar con el arreglo indicado
			elif(self.language == 26):
				# Se recorre todo el tamaño de la clave, al finalizar, se toma la primera letra del texto en descifrado
				if(cont < tamClave):
					letraNumberClave = alfabeto.numberToCharacterEnglish[self.clave[(cont):(cont+1)]]
				else:
					letraNumberClave = alfabeto.numberToCharacterEnglish[textoDescif[(contAux):(contAux+1)]]
					contAux += 1
				# Se extrae la posición de la letra y se realiza la operación de descifrado
				letraNumberMsj = alfabeto.numberToCharacterEnglish[self.textoCifrado[(cont):(cont+1)]]
				textoDescif += alfabeto.characterToNumberEnglish[(letraNumberMsj - letraNumberClave) % 26]
			elif(self.language == "ascii"):
				# Se recorre todo el tamaño de la clave, al finalizar, se toma la primera letra del texto en descifrado
				if(cont < tamClave):
					numberLetraClave = alfabeto.characterToNumberBase64[clave[(cont):(cont+1)]]
				else:
					numberLetraClave = alfabeto.characterToNumberBase64[textoDescif[(contAux):(contAux+1)]]
					contAux += 1
				# Se extrae la posición de la letra y se realiza la operación de descifrado
				numberLetraMsj = alfabeto.characterToNumberBase64[texto[(cont):(cont+1)]]
				textoDescif += alfabeto.numberToCharacterBase64[(numberLetraMsj - numberLetraClave) % 64]

			
			cont += 1
		# Se crea un archivo con el texto descifrado
		if(self.language == "ascii"):
			textoDescif = alfabeto.desCodBase64ToTexto(textoDescif)
		
		return textoDescif

	def toStringMenu(self):
		#cadena.center(50, "=") 
		long_linea_va = 80
		salto = "\n"
		head_algo_dos = "VIGENERE (AUTOCLAVE)"
		cabecera_va = "-"*long_linea_va
		linea_va = "|"+(" "*(long_linea_va-2))+"|"
		menu = cabecera_va+salto+linea_va+salto
		menu += "|"+(" "*26)+head_algo_dos+(" "*32)+"|"+salto+linea_va+salto
		menu += "|   Sintaxis: toolCripto.py -va <modo> <archivoEntrada> <archivoLlave>"+(" ")*9+"|"+salto
		menu += "|   <modo>:"+(" "*68)+"|"+salto
		menu += "|        -c cifrar archivo"+(" "*53)+"|"+salto
		menu += "|        -d cifrar archivo"+(" "*53)+"|"+salto+linea_va+salto
		menu += "|        <archivoEntrada>: Nombre del archivo a cifrar o descifrar"+(" "*13)+"|"+salto
		menu += "|        <archivoMascara>: Nombre del archivo que contiene la mascara"+(" "*10)+"|"+salto
		menu += "|        Si <modo> -c, el archivo de salida es <archivoEntrada>.cif"+(" "*12)+"|"+salto
		menu += "|        Si <modo> -d, el archivo de salida es <archivoEntrada>.dec"+(" "*12)+"|"+salto+linea_va+salto
		menu += "|   Ejemplo:"+(" "*67)+"|"+salto
		menu += "|     Cifrar:    toolCripto.py -va -c <archivoEntrada>.txt <archivoLlave>.key  "+"|"+salto
		menu += "|     Descifrar: toolCripto.py -va -d <archivoEntrada>.cif <archivoLlave>.key  "+"|"+salto+linea_va+salto+cabecera_va
		return menu

	
