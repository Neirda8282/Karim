# (C) Fabrice Sincère
import wave
import binascii

NomFichier = input('Entrer le nom du fichier : ')
Monson = wave.open(NomFichier,'r')	# instanciation de l'objet Monson

print("\nNombre de canaux :",Monson.getnchannels())
print("Taille d'un échantillon (en octets):",Monson.getsampwidth())
print("Fréquence d'échantillonnage (en Hz):",Monson.getframerate())
print("Nombre d'échantillons :",Monson.getnframes())
print("Type de compression :",Monson.getcompname())

TailleData = Monson.getnchannels()*Monson.getsampwidth()*Monson.getnframes()

print("Taille du fichier (en octets) :",TailleData + 44)
print("Nombre d'octets de données :",TailleData)


Monson.setpos(0)
T=[]
R=[]
for i in range(0,Monson.getnframes()):
    R.append(Monson.tell())
    T.append(binascii.hexlify(Monson.readframes(1)))

Monson.close()
print(T)
