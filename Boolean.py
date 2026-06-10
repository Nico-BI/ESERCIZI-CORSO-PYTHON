#Confronta se il numero è positivo

x=int(input("Inserisci il numero che vorresti controllare se positivo: "))
risultato = x > 0 
print(risultato)


#Confronto tra due stringhe

s1 = str(input("Inserisci la tua prima stringa: "))
s2 = str(input("Inserisci la tua seconda stringa: "))
print ( s1 == s2 ) 


#Confronta se due numeri sono positivi

a = int(input("Inserisci il primo numero: "))
b = int(input("Inserisci il secondo numero: "))

risultato = (a > 0) and (b > 0)
print(risultato)


#Controlla se l'utente può guidare

età=int(input("Inserisci la tua età: "))
patente=str(input("Hai la patente? Rispondi con 'si' o 'no': "))
print(età>=18 and patente=='si')


#Entrata in biblioteca 

tempo=int(input("Inserisci da quanti mesi hai il libro: "))
limite=3
premium=str(input("Hai l'abbonamento PREMIUM? Rispondi con 'si' o 'no': "))
print(tempo<= limite or premium=='si')