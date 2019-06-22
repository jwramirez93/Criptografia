from time import time
from Vigenere import Vigenere
from MascaraRotativa import MascaraRotativa
import sys, json

# -*- coding: utf-8 -*-

# Variables del menu principal
long_linea_main = 70
cabecera = "-"*long_linea_main
salto = "\n"
linea = "|"+(" "*(long_linea_main-2))+"|"
titulo = "ALGORITMOS CRIPTOGRAFICOS"
subtitulo = "sintaxis: toolCripto.py <algoritmo>"
tit_algs = "<algoritmo>:"
tit_algo_uno = "-mr   Mascara Rotativa"
tit_algo_dos = "-va   Algoritmo de Vigenere (Autoclave)"
tit_algo_tres = "consultar la ayuda de un algoritmo en especifico:"
tit_config = "si desea cambiar el tamaño del alfabeto:"
tit_help_config_uno = "sintaxis: toolCripto.py -config -tamAlf 26|27"
tit_help_uno = "sintaxis: toolCripto.py <algoritmo>"
tit_help_dos = "toolCripto.py <algoritmo> -a"

# Variables del menu de ayuda de mascara rotativa
long_linea_mr = 80
cabecera_mr = "-"*long_linea_mr
linea_mr = "|"+(" "*(long_linea_mr-2))+"|"
head_algo_uno = "MASCARA ROTATIVA"

# Cargo el archivo de configuracion para validar el lenguaje
configFile = ""
archivo = open("config.json", "r")
for lineaFileConfig in archivo.readlines(): 
	configFile = lineaFileConfig
archivo.close()
configFile = json.loads(configFile)
language = configFile['tamAlfabeto']

# Se valida que el usuario no ingresó parametros y se muestra el menú principal
if(len(sys.argv) <= 1):

	menu = cabecera+salto+linea+salto
	menu += "|"+(" "*15)+titulo+(" "*28)+"|"+salto
	menu += linea+salto
	menu += "|"+(" "*5)+subtitulo+(" "*28)+"|"+salto
	menu += linea+salto+"|"+(" "*5)+tit_algs+(" "*51)+"|"+salto
	menu += "|"+(" "*10)+tit_algo_uno+(" "*36)+"|"+salto
	menu += "|"+(" "*10)+tit_algo_dos+(" "*19)+"|"+salto+linea+salto
	menu += "|"+(" "*5)+tit_algo_tres+(" "*14)+"|"+salto
	menu += "|"+(" "*20)+tit_help_uno+(" "*13)+"|"+salto
	menu += "|"+(" "*30)+tit_help_dos+(" "*10)+"|"+salto+linea+salto
	menu += "|"+(" "*5)+tit_config+(" "*23)+"|"+salto
	menu += "|"+(" "*15)+tit_help_config_uno+(" "*8)+"|"+salto+linea+salto+cabecera
	print(menu)

else:
	# Se valida que el usuario escogió la opción de algoritmo Vigenere Autoclave
	if(sys.argv[1] == "-va"):

		vigenere = Vigenere()
		# En caso de que el usuario no coloque el parametro de ayuda y no hayan mas parametros,
		# de igual forma se muestra el menú
		if(len(sys.argv)) <= 3:

			sys.argv.insert(2, "-a")
		# Se valida que el usuario escogió el menú de ayuda y se muestra
		else:
			# Se realiza el cargue de la clave en claro y se quitan los espacios en blanco
			archivoClave = open(sys.argv[4], "r",encoding='ISO-8859-1')
			for lineaFileClave in archivoClave.readlines(): 
				clave = lineaFileClave
			archivoClave.close()
			clave = clave.replace(" ", "")
			tamClave = len(clave)
		# Se valida que el usuario escogió la opción de ayuda para algoritmo Virgene (Autoclave)
		if(sys.argv[2] == "-a"):

			menu_algo_dos = vigenere.toStringMenu()
			print(menu_algo_dos)
		# Se valida que el usuario escogio la opción de cifrado
		elif(sys.argv[2] == '-c'):
			
			msj_salida = salto+"Procesando..."+salto+salto
			print(msj_salida)
			# Se comienza a contar el tiempo de ejecución
			start_time = time()

			# Se realiza el cargue del archivo en claro y se quitan los espacios en blanco

			#archivoIni = open(sys.argv[3], "r", errors='ignore')
			archivoIni = open(sys.argv[3],"r", encoding='ISO-8859-1')
			for lineaFileIni in archivoIni.readlines(): 
				texto = lineaFileIni
			archivoIni.close()
			texto = texto.replace(" ", "")

			vigenere.textoClaro = texto
			vigenere.clave = clave
			vigenere.language = language
			texto = vigenere.cifrar()
			# Se crea un archivo con extensión *.cif con el texto cifrado
			nombreArchivo = sys.argv[3]
			nombreArchivo = nombreArchivo.split('.')
			nombreArchivo = nombreArchivo[0]
			#fileCif = open(nombreArchivo+".cif","w+", errors='ignore')
			fileCif = open(nombreArchivo+".cif","w+", encoding='ISO-8859-1')
			fileCif.write(texto)
			fileCif.close()

			# Se finaliza el tiempo de ejecución y se muestra al usuario
			elapsed_time = time() - start_time
			msj_salida = ("-"*50)+salto
			msj_salida += ": OPERACION TERMINADA CON EXITO !!"+salto+salto
			msj_salida += "      Se tardo:"+str(elapsed_time)+" segundos"+salto
			msj_salida += ("-"*50)
			print(msj_salida)
		# Se valida que el usuario escogio la opción de descifrado
		elif(sys.argv[2] == '-d'):

			msj_salida = salto+"Procesando..."+salto+salto
			print(msj_salida)
			# Se comienza a contar el tiempo de ejecución
			start_time = time()
			# Se carga y lee el archivo cifrado
			textoCif = ""
			fileCif = open(sys.argv[3], "r")
			for lineaFile in fileCif.readlines(): 
				textoCif = lineaFile
			fileCif.close()

			vigenere.textoCifrado = textoCif
			vigenere.clave = clave
			vigenere.language = language
			textoDescif = vigenere.descifrar()
			
			nombreArchivo = sys.argv[3]
			nombreArchivo = nombreArchivo.split('.')
			nombreArchivo = nombreArchivo[0]
			#fileDes = open(nombreArchivo+".dec","w+", errors='ignore')
			fileDes = open(nombreArchivo+".dec","w+", encoding='ISO-8859-1')			
			fileDes.write(textoDescif)
			fileDes.close()

			# Se valida el tiempo de ejecución total y se muestra el usuario
			elapsed_time = time() - start_time
			msj_salida = ("-"*50)+salto
			msj_salida += ": OPERACION TERMINADA CON EXITO !!"+salto+salto
			msj_salida += "      Se tardo:"+str(elapsed_time)+" segundos"+salto
			msj_salida += ("-"*50)
			print(msj_salida)
	
	elif(sys.argv[1] == "-mr"):

		mascaraRotativa = MascaraRotativa()

		if(len(sys.argv)) <= 3:

			sys.argv.insert(2, "-a")
		# Se valida que el usuario escogió el menú de ayuda y se muestra
		else:
			# Se realiza el cargue de las perforaciones
			archivoClave = open(sys.argv[4], "r")
			for lineaFileClave in archivoClave.readlines(): 
				perforaciones = lineaFileClave
			archivoClave.close()
		# Se valida que el usuario escogió la opción de ayuda para algoritmo Virgene (Autoclave)
		if(sys.argv[2] == "-a"):

			menu_algo_dos = mascaraRotativa.toStringMenu()
			print(menu_algo_dos)
		# Se valida que el usuario escogio la opción de cifrado
		elif(sys.argv[2] == '-c'):
			
			msj_salida = salto+"Procesando..."+salto+salto
			print(msj_salida)
			# Se comienza a contar el tiempo de ejecución
			start_time = time()

			# Se realiza el cargue del archivo en claro y se quitan los espacios en blanco

			#archivoIni = open(sys.argv[3], "r", errors='ignore')
			archivoIni = open(sys.argv[3], "r", encoding='ISO-8859-1')			
			for lineaFileIni in archivoIni.readlines(): 
				texto = lineaFileIni
			archivoIni.close()
			texto = texto.replace(" ", "")

			mascaraRotativa.textoClaro = texto
			mascaraRotativa.perforaciones = perforaciones
			texto = mascaraRotativa.cifrar()
			# Se crea un archivo con extensión *.cif con el texto cifrado
			nombreArchivo = sys.argv[3]
			nombreArchivo = nombreArchivo.split('.')
			nombreArchivo = nombreArchivo[0]
			#fileCif = open(nombreArchivo+".cif","w+", errors='ignore')
			fileCif = open(nombreArchivo+".cif","w+", encoding='ISO-8859-1')
			fileCif.write(texto)
			fileCif.close()

			# Se finaliza el tiempo de ejecución y se muestra al usuario
			elapsed_time = time() - start_time
			msj_salida = ("-"*50)+salto
			if(len(texto) < 1):
				msj_salida += ": ERROR !!"+salto+salto
			else:
				msj_salida += ": OPERACION TERMINADA CON EXITO !!"+salto+salto
			msj_salida += "      Se tardo:"+str(elapsed_time)+" segundos"+salto
			msj_salida += ("-"*50)
			print(msj_salida)
		# Se valida que el usuario escogio la opción de descifrado
		elif(sys.argv[2] == '-d'):

			msj_salida = salto+"Procesando..."+salto+salto
			print(msj_salida)
			# Se comienza a contar el tiempo de ejecución
			start_time = time()
			# Se carga y lee el archivo cifrado
			textoCif = ""
			fileCif = open(sys.argv[3], "r")
			for lineaFile in fileCif.readlines(): 
				textoCif = lineaFile
			fileCif.close()

			mascaraRotativa.textoCifrado = textoCif
			mascaraRotativa.perforaciones = perforaciones
			textoDescif = mascaraRotativa.descifrar()
			
			nombreArchivo = sys.argv[3]
			nombreArchivo = nombreArchivo.split('.')
			nombreArchivo = nombreArchivo[0]
			#fileDes = open(nombreArchivo+".dec","w+", errors='ignore')
			fileDes = open(nombreArchivo+".dec","w+", encoding='ISO-8859-1')
			fileDes.write(textoDescif)
			fileDes.close()

			# Se valida el tiempo de ejecución total y se muestra el usuario
			elapsed_time = time() - start_time
			msj_salida = ("-"*50)+salto
			msj_salida += ": OPERACION TERMINADA CON EXITO !!"+salto+salto
			msj_salida += "      Se tardo:"+str(elapsed_time)+" segundos"+salto
			msj_salida += ("-"*50)
			print(msj_salida)

	# Se valida que el usuario escogio la opción de configuracion
	elif(sys.argv[1] == "-config"):
		# Se valida que el usuario escogio la opción para configurar el tamaño del alfabeto
		if(sys.argv[2] == "-tamAlf"):
			
			tam = sys.argv[3]
			# Se valida que el usuario escogio una opción correcta para el tamaño del alfabeto
			if(tam == "26" or tam == "27"):
				# Se abre el archivo de configuracion
				archivo = open("config.json", "r")
				for lineaFileConfig in archivo.readlines(): 
					configFile = lineaFileConfig
				archivo.close()
				configFile = json.loads(configFile)
				configFile['tamAlfabeto'] = int(tam)
				# Se re escribe el archivo de configuracion
				archivo = open("config.json", "w+")
				configFile = json.dumps(configFile)
				archivo.write(configFile)
				archivo.close()
				
				print("Cambio realizado")
			# Si el usuario no escogio una opción correcta para el tamaño del alfabeto se muestra un mensaje
			else:

				print("El tamaño de alfabeto ingresado está incorrecto")
		# Si el usuario no escogio una opción valida para el algoritmo de Vigenere (Autoclave) se muestra un mensaje
		else:

			print("No escogió una opción valida")
	# Si el usuario no escogio una opción valida se muestra un mensaje
	else:
		# Si el usuario no escogio una opción valida se muestra un mensaje
		salida = "La opción ("+sys.argv[1]+") no existe"
		print(salida)

	
	
