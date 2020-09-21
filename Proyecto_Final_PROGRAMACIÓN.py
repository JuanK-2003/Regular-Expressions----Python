import re

while True:
     print ("\n")
     cadena = input("\t\t\tIngrese texto: ")
     print ("\n\t\t\t El texto contiene","-",len(cadena)-cadena.count(" "),"-","caracteres sin espacios")
     mayusculas = re.sub('[^A-Z]','',cadena) + re.sub('[^Á-Ú]', '', cadena)
     print ("\n\t\t\t El total de mayusculas es: ", str(len(mayusculas) + cadena.count('Ü')))
     minusculas = re.sub('[^a-z]','',cadena) + re.sub('[^á-ú]', '', cadena)
     print ("\n\t\t\t El total de minusculas es: ",str(len(minusculas) + cadena.count('ü')))
     tildes = re.sub('[^á-ú]', '', cadena) + re.sub('[^Á-Ú]', '', cadena)
     print ('\n\t\t\t El total de letras con tildes es: ', str(len(tildes)))
     print ("\n\t\t\t Tiene ", cadena.count(" "),"espacios")
     numeros = re.sub('[^\d]','',cadena)
     print ("\n\t\t\t El total de números es: ",str(len(numeros)))

     repetir = input("\n\t\t\t ¿Desea ingresar una nueva cadena? ").lower()

     while repetir != 'si' and repetir != 'no':
         print(' \t\t\tERROR: Datos inválidos!')
         repetir = input("\n\t\t\t ¿Desea ingresar una nueva cadena? ").lower()

     if repetir == 'no':
         break