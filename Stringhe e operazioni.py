#Inserisci una frase e inverti l'ordine delle parole
frase=str(input("Inserisci una frase: "))
contrario=frase[::-1]
print(f"La tua frase al contrario è: {contrario}")

#Elimina gli spazi fra le lettere e verifica se palindroma

nospazi=frase.replace(" ", "")
print(f"La tua frase senza spazi è: {nospazi}")
palindroma=contrario.replace(" ","")
if nospazi==palindroma:
    print("La tua frase è palindroma") 
else:
    print("La tua frase non è palindroma")

#Primo, ultimo carattere e lunghezza

print("Il primo carattere della tua frase è: ", frase[0])     
print("L'ultimo carattere della tua frase è: ", frase[-1])
print(f"La lunghezza della tua frase è di {len(frase)} caratteri")   


#Stampa in maiuscolo o minuscolo

print("La tua frase in MAIUSCOLO è: ", frase.upper())  
print("La tua frase in minuscolo è: ", frase.lower())  


#conteggio di una lettera

lettera = str(input("Inserisci la lettera che vorresti contare: "))
conteggio = frase.count(lettera)
print(f"La lettera '{lettera}' compare {conteggio} volte.")  

#Verifica lettera di inizio e fine

inizio=str(input("Indovina con quale lettera inizia la tua frase: "))
print(frase.startswith(inizio))  
fine=str(input("Indovina con quale lettera finisce la tua frase: "))
print(frase.endswith(fine))    


#Cambio di lettere
prima = str(input("Inserisci la lettera che vorresti sostituire: "))
dopo = str(input("Inserisci la lettera che vorresti inserire: "))
print("La tua frase con lo scambio di lettere è: ", frase.replace(prima,dopo))


#Ripetere una porzione di testo

porzione=int(input("Inserisci il numero di lettere che vorresti ripetere partendo dall'inizio: "))
ripetizioni=int(input("Inserisci quante volte lo vorresti ripetuto: "))
print(frase[:porzione] * ripetizioni)  
