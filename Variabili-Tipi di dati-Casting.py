#Stampa il contenuto delle variabile

nome = "Nicolas"
età = 37
città = "Cremona"

print(nome, età, città)


#Stampa il dato modificato della variabile

x = 5
print(x)
x = 10
print(x) 


#Operazione con variabili

x = 10
y = 20
print("La somma è:", x + y)  


#Scambio dei dati tra variabili

x = 20
y = 15

x, y = y, x
print(x, y)  


#Area rettangolo 

base = 5
altezza = 10
area = base * altezza
print("Area rettangolo:", area)  


#Operazioni tra diversi tipi di variabili 

a = 10
b = 3.5
print(a+b,type(a + b))  


#Media tra numeri

x, y, z = 10, 40, 30
media = (x + y + z) / 3
print("Media:", float(media))  


#Unisci due stringhe 

s1 = "Mi piace "
s2 = " giocare a calcio"
print(s1 + s2)  


#Ripeti più volte una stringa 

print("Ciao " * 3)  


#Stampa se vero o falso 

a = 15
b = 30
c = 45 
print(a < b)
print(b > c) 
print(a < c)  


#Casting di un intero 

x = 10
y = float(x)
print(y)  


#Casting di una stringa

n = "4550"
s = int(n)
print( " il numero è: " , s)  


#verifica se vero o falso

print (bool(10))
print (bool(0))
print (bool(-100))
print (bool(""))
