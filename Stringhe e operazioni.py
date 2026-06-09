#Inserisci una frase e inverti l'ordine delle parole
frase=str(input("Inserisci una frase: "))
print("La tua frase al contrario è: ", frase[::-1]) 


#Stampa il primo e l'ultimo carattere 

print("Il primo carattere della tua frase è: ", frase[0])     
print("L'ultimo carattere della tua frase è: ", frase[-1])   


#Stampa in maiuscolo o minuscolo

print("La tua frase in MAIUSCOLO è: ", frase.upper())  
print("La tua frase in minuscolo è: ", frase.lower())  


#conteggio di una lettera

lettera = str(input("Inserisci la lettera che vorresti contare: "))
conteggio = frase.count(lettera)
print(f"La lettera '{lettera}' compare {conteggio} volte.")  

#Verifica lettera di inizio e fine

inizio=str(input("Con quale lettera inizia la frase: "))
print(frase.startswith(inizio))  
fine=str(input("Con quale lettera finisce la frase: "))
print(frase.endswith(fine))    


#Elimina gli spazi fra le lettere

print("La tua frase senza spazi è: ", frase.replace(" ", ""))  


#Ripetere una porzione di testo

porzione=int(input("Inserisci il numero di lettere che vorresti ripetere partendo dall'inizio: "))
ripetizioni=int(input("Inserisci quante volte lo vorresti ripetuto: "))
print(frase[:porzione] * ripetizioni)  
