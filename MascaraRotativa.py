import math
import random
import string

class MascaraRotativa:

	def __init__(self):
		self.textoClaro = ''
		self.textoCifrado = ''
		self.perforaciones = ''

	def cifrar(self):
		mensaje = self.textoClaro
		mensaje = mensaje.replace(" ", "")
		tamMatriz = math.ceil(math.sqrt(len(mensaje))) + 500# + math.ceil((len(mensaje)/20))
		cantPerforaciones = math.ceil(len(mensaje)/4)

		'''archivoClave = open("perforacionesMasRot.key", "r", errors='ignore')
		for lineaFileCla in archivoClave.readlines(): 
			perforacion = lineaFileCla
		archivoClave.close()'''
		perforacion = self.perforaciones
		perforacion = perforacion.split(',')
		perforacion = list(map(int, perforacion))
		perforacion = sorted(perforacion)

		tamPerforaciones = len(perforacion)
		matrizPer = dict()
		#if(tamPerforaciones != cantPerforaciones):
		#	print("Las perforaciones que ingresó son incorrectas, deben ser: "+str(cantPerforaciones)+" e ingresó: "+str(tamPerforaciones))
		#	return ""

		maxPerforacion = max(perforacion)
		tamMaxMatriz = tamMatriz*tamMatriz

		if(maxPerforacion > tamMaxMatriz):
			print("La perforacion que ingresó en la posición "+str(maxPerforacion)+" es incorrecta, la posición maxima debe ser: "+str(tamMaxMatriz))
			return ""

		#CREACION DE MATRIZ
		cont = 1
		for i in range(1,tamMatriz+1):
			matrizPer.update({i: {cont:""}})
			for j in range(1,tamMatriz+1):
				matrizPer[i].update({cont:""})
				cont += 1

		#MARCACION DE PERFORACIONES
		posLetraMsj = 1
		for i in perforacion:
			for j in matrizPer:
				llaves = list(matrizPer[j].keys())
				ultimoElementRow = llaves[-1]
				if(i <= ultimoElementRow):
					if(len(matrizPer[j][i]) > 0):
						print("La perforación "+str(i)+" se encuentra repetida")
						return ""
					matrizPer[j][i] = mensaje[(posLetraMsj-1):posLetraMsj]
					posLetraMsj += 1
					break

		#GIRO 45
		posLetraMsj = tamPerforaciones+1
		contFila = 1
		for i in perforacion:
			contFila = 1
			for j in matrizPer:
				lista = list(matrizPer[j])
				llaves = list(matrizPer[j].keys())
				ultimoElementRow = llaves[-1]
				if(i <= ultimoElementRow):

					pos = (lista.index(i)+1)
					fila = pos
					col = ((fila - 1) * tamMatriz) + (tamMatriz - (contFila-1))
					
					if(len(matrizPer[fila][col]) > 0):
						print("La perforacion "+str(fila)+":"+str(i)+" colisionó en la primera rotación")
						return ""
					matrizPer[fila][col] = mensaje[(posLetraMsj-1):posLetraMsj]
					posLetraMsj += 1
					break
				
				contFila += 1

		#GIRO 90
		posLetraMsj = (tamPerforaciones*2)+1
		contFila = 1
		for i in perforacion:
			contFila = 1
			for j in matrizPer:
				lista = list(matrizPer[j])
				llaves = list(matrizPer[j].keys())
				ultimoElementRow = llaves[-1]
				if(i <= ultimoElementRow):
					pos = (lista.index(i)+1)
					fila = (tamMatriz + 1) - contFila
					col = ((fila - 1) * tamMatriz) + (tamMatriz - (pos-1))
					if(len(matrizPer[fila][col]) > 0):
						print("La perforacion "+str(i)+" colisionó en la segunda rotación")
						return ""
					matrizPer[fila][col] = mensaje[(posLetraMsj-1):posLetraMsj]
					posLetraMsj += 1
					break
				
				contFila += 1

		#GIRO 135
		posLetraMsj = (tamPerforaciones*3)+1
		contFila = 1
		for i in perforacion:
			contFila = 1
			for j in matrizPer:
				lista = list(matrizPer[j])
				llaves = list(matrizPer[j].keys())
				ultimoElementRow = llaves[-1]
				if(i <= ultimoElementRow):
					pos = (lista.index(i)+1)
					fila = (tamMatriz+1)-pos
					col = ((tamMatriz-pos)*tamMatriz)+contFila
					if(len(matrizPer[fila][col]) > 0):
						print("La perforacion "+str(col)+" colisionó en la tercera rotación")
						return ""
					matrizPer[fila][col] = mensaje[(posLetraMsj-1):posLetraMsj]
					posLetraMsj += 1
					break
				
				contFila += 1

		textoCif = ""
		for subMatriz in matrizPer:
			for i in matrizPer[subMatriz]:
				pos = matrizPer[subMatriz][i]
				if(len(pos) < 1):
					textoCif += random.choice(string.ascii_letters).upper()
				else:
					textoCif += pos

		return textoCif

	def descifrar(self):

		mensaje = self.textoCifrado
		perforacion = self.perforaciones

		perforacion = perforacion.split(',')
		perforacion = list(map(int, perforacion))
		perforacion = sorted(perforacion)

		tamMatriz = math.ceil(math.sqrt(len(perforacion)*4)) + 500#math.ceil(((len(perforacion)*4)/10))
		matrizPer = dict()

		#CREACION DE MATRIZ
		cont = 1
		posLetraMsj = 1
		for i in range(1,tamMatriz+1):
			matrizPer.update({i: {cont:""}})
			for j in range(1,tamMatriz+1):
				matrizPer[i].update({cont:mensaje[(posLetraMsj-1):posLetraMsj]})
				cont += 1
				posLetraMsj += 1

		mensajeDecifrado = []
		for i in matrizPer:
			for j in perforacion:
				llaves = list(matrizPer[i].keys())
				ultimoElementRow = llaves[-1]
				primerElementRow = llaves[0]
				if(j <= ultimoElementRow and j>= primerElementRow):
					mensajeDecifrado.append(matrizPer[i][j])

		#GIRO 45
		contFila = 1
		for i in perforacion:
			contFila = 1
			for j in matrizPer:
				lista = list(matrizPer[j])
				llaves = list(matrizPer[j].keys())
				ultimoElementRow = llaves[-1]
				if(i <= ultimoElementRow):
					pos = (lista.index(i)+1)
					fila = pos
					col = ((fila - 1) * tamMatriz) + (tamMatriz - (contFila-1))
					mensajeDecifrado.append(matrizPer[fila][col])		
					break
				
				contFila += 1

		#GIRO 90
		contFila = 1
		for i in perforacion:
			contFila = 1
			for j in matrizPer:
				lista = list(matrizPer[j])
				llaves = list(matrizPer[j].keys())
				ultimoElementRow = llaves[-1]
				if(i <= ultimoElementRow):
					pos = (lista.index(i)+1)
					fila = (tamMatriz + 1) - contFila
					col = ((fila - 1) * tamMatriz) + (tamMatriz - (pos-1))
					mensajeDecifrado.append(matrizPer[fila][col])		
					break
				
				contFila += 1

		#GIRO 135
		contFila = 1
		for i in perforacion:
			contFila = 1
			for j in matrizPer:
				lista = list(matrizPer[j])
				llaves = list(matrizPer[j].keys())
				ultimoElementRow = llaves[-1]
				if(i <= ultimoElementRow):
					pos = (lista.index(i)+1)
					fila = (tamMatriz+1)-pos
					col = ((tamMatriz-pos)*tamMatriz)+contFila
					mensajeDecifrado.append(matrizPer[fila][col])		
					break		
				contFila += 1


		# Para trabajarlo como Cadena. remplazar mensajeDecifrado.append por mensajeDecifrado += y declararlo como mensajeDecifrado = ""
		tempStr = ""
		for x in mensajeDecifrado:
			tempStr+=x

		return tempStr

	def toStringMenu(self):
		#cadena.center(50, "=") 
		long_linea_va = 80
		salto = "\n"
		head_algo_dos = "MASCARA ROTATIVA"
		cabecera_va = "-"*long_linea_va
		linea_va = "|"+(" "*(long_linea_va-2))+"|"
		menu = cabecera_va+salto+linea_va+salto
		menu += "|"+(" "*26)+head_algo_dos+(" "*36)+"|"+salto+linea_va+salto
		menu += "|   Sintaxis: toolCripto.py -va <modo> <archivoEntrada> <archivoMascara>"+(" ")*7+"|"+salto
		menu += "|   <modo>:"+(" "*68)+"|"+salto
		menu += "|        -c cifrar archivo"+(" "*53)+"|"+salto
		menu += "|        -d cifrar archivo"+(" "*53)+"|"+salto+linea_va+salto
		menu += "|        <archivoEntrada>: Nombre del archivo a cifrar o descifrar"+(" "*13)+"|"+salto
		menu += "|        <archivoMascara>: Nombre del archivo que contiene la mascara"+(" "*10)+"|"+salto
		menu += "|        Si <modo> -c, el archivo de salida es <archivoEntrada>.cif"+(" "*12)+"|"+salto
		menu += "|        Si <modo> -d, el archivo de salida es <archivoEntrada>.dec"+(" "*12)+"|"+salto+linea_va+salto
		menu += "|   Ejemplo:"+(" "*67)+"|"+salto
		menu += "|    Cifrar:    toolCripto.py -mr -c <archivoEntrada>.txt <archivoMascara>.key "+"|"+salto
		menu += "|    Descifrar: toolCripto.py -mr -d <archivoEntrada>.cif <archivoMascara>.key "+"|"+salto+linea_va+salto+cabecera_va
		return menu
