#Verifica se un numero è positivo o negativo

x=float(input("Inserisci un numero:"))

if x > 0:
    print ("È un numero positivo")
elif x < 0:
    print ("È un numero negativo")
else:
    print("Zero")


#Confronta due numeri

a = float(input("Inserisci il primo numero:"))
b = float(input("Inserisci il secondo numero numero:"))

if a > b:
    print (f"{a} è maggiore di {b}")
else: 
    print (f"{b} è maggiore di {a}")


#Dichiara l'età

età=int(input("Inserisci l'età:"))

if età >= 18:
    print ("sei maggiorenne")
else:
    print ("sei minorenne")


#Multiplo di 3

n = int(input("Inserisci un numero:"))
if n % 3 == 0:
    print("È un multiplo di 3")
else:
    print("Non èmultiplo di 3")


# Esame con voto

voto=float(input("Inserisci il tuo voto:"))
if voto >= 18:
    print("Esame superato")
else:
    print("Bocciato")


#Vocali e Consonanti

c =str(input("Inserisci una lettera:")) 
if c in "aeiou":
    print("È una vocale")
else:
    print("È una consonante")



#Confronto tra tre numeri

a = float(input("Inserisci il primo numero:"))
b = float(input("Inserisci il secondo numero:"))
c = float(input("Inserisci il terzo numero:"))

if a > b and a > c:
    print("a è il maggiore")
elif b > a and b > c:
    print("b è il maggiore")
elif c > a and c > b:
    print("c è il maggiore")
else:
    print("Sono tutti uguali")

#Prezzo biglietto

eta =int(input("Inserisci l'età:"))
if eta < 12:
    prezzo = 5
elif eta < 65:
    prezzo = 10
else:
    prezzo = 7
print("Prezzo biglietto:", prezzo, "€")


#Tipi di triangoli

a = int(input("Inserisci la misura del primo lato:"))
b = int(input("Inserisci la misura del secondo lato:"))
c = int(input("Inserisci la misura del terzo lato:"))

if a == b == c:
    print("Triangolo equilatero")
elif a == b or b == c or a == c:
    print("Triangolo isoscele")
else:
    print("Triangolo scaleno")


#fascie d'età

età=int(input("Inserisci la tua età:"))

if età<18:
    print("Sei minorenne")
elif età>=18 and età<65:
    print("Sei adulto")
else:
    print("Sei anziano")